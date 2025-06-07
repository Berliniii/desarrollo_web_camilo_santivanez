from flask import Flask, request, render_template, url_for, session, redirect, jsonify
from flask_cors import cross_origin
from utils.validations import *
from database import db
from werkzeug.utils import secure_filename
import hashlib
import filetype
import os
from markupsafe import escape

UPLOAD_FOLDER = 'static/uploads'

app = Flask(__name__)

# Configuración de la base de datos
db_config = {
    'host': 'localhost',
    'user': 'cc5002',
    'password': 'programacionweb',
    'database': 'tarea2'
}

# Configuración para subir archivos
UPLOAD_FOLDER = 'static/uploads'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/', methods=["GET"])
def index():
    actividades = db.get_actividades_recientes(limit=5)

    data = []
    for actividad in actividades:
        # Procesar temas y fotos
        tema = actividad.temas[0].tema if actividad.temas else "-"
        foto = actividad.fotos[0].ruta_archivo if actividad.fotos else None
        foto_url = url_for('static', filename=foto) if foto else None

        data.append({
            "inicio": actividad.dia_hora_inicio.strftime('%Y-%m-%d %H:%M'),
            "termino": actividad.dia_hora_termino.strftime('%Y-%m-%d %H:%M') if actividad.dia_hora_termino else "",
            "comuna": actividad.comuna.nombre if actividad.comuna else "-",
            "sector": actividad.sector,
            "tema": tema,
            "foto_url": foto_url
        })

    return render_template('index.html', actividades=data)

@app.route('/listado')
def listado():
    page = request.args.get('page', 1, type=int)
    per_page = 5
    
    # Obtener total de actividades para la paginación
    total_actividades = db.get_total_actividades()
    total_pages = (total_actividades + per_page - 1) // per_page
    
    # Obtener actividades de la página actual
    actividades = db.get_actividades_paginadas(page=page, per_page=per_page)
    
    # Formatear datos para el frontend
    data = []
    for actividad in actividades:
        tema = actividad.temas[0].tema if actividad.temas else "-"
        data.append({
            "id": actividad.id,
            "inicio": actividad.dia_hora_inicio.strftime('%Y-%m-%d %H:%M'),
            "termino": actividad.dia_hora_termino.strftime('%Y-%m-%d %H:%M') if actividad.dia_hora_termino else "",
            "comuna": actividad.comuna.nombre,
            "sector": actividad.sector,
            "tema": tema,
            "organizador": actividad.nombre,
            "fotos": len(actividad.fotos)
        })
    
    return render_template('listado.html', 
                         actividades=data,
                         current_page=page,
                         total_pages=total_pages)

@app.route('/estadisticas')
def estadisticas():
    return render_template('estadisticas.html')

@app.route('/api/comunas/<int:region_id>')
def api_comunas(region_id):
    comunas = db.get_comunas_by_region_id(region_id)
    return jsonify([{"id": c.id, "nombre": c.nombre} for c in comunas])

@app.route('/agregar_actividad', methods=["GET", "POST"])
def agregar():
    mensaje = None
    regiones = db.get_all_regiones() 
    temas = [
            "música", "deporte", "ciencias", "religión", "política",
            "tecnología", "juegos", "baile", "comida", "otro"
        ]
    if request.method == "POST":
        # Obtener datos del formulario
        comuna_id = request.form.get("select-comuna")
        sector = (request.form.get("sector"))
        nombre = request.form.get("nombre_organizador")
        email = (request.form.get("email-organizador"))
        celular = request.form.get("celu-organizador")
        dia_hora_inicio = request.form.get("dia-hora-inicio")
        dia_hora_termino = request.form.get("dia-hora-termino")
        descripcion = (request.form.get("descripcion-actividad"))

        # ---Validaciones---
        errores = []

        #Comuna
        if not validate_comuna(comuna_id):
            errores.append("Comuna inválida")
        #Sector
        if not validate_sector(sector):
            errores.append("Sector debe tener máximo 100 caracteres")
        #Nombre    
        if not validate_nombre(nombre):
            errores.append("Nombre inválido o muy largo (máximo 200 caracteres)")
        #Email    
        if not validate_email(email):
            errores.append("Email inválido")
        #Celular    
        if celular and not validate_celular(celular):
            errores.append("Formato de celular inválido (+569.XXXXXXXX)")
        #Fechas    
        if not validate_fechas(dia_hora_inicio, dia_hora_termino):
            errores.append("Fechas inválidas o término antes que inicio")
        #Tema   
        if not any(request.form.get(tema) for tema in temas):
            errores.append("Debe seleccionar al menos un tema.")
        
        #Fotos
        # Validar fotos
        for i in range(1, 6):
            file = request.files.get(f"foto{i}")
            if file and file.filename:
                if not validate_conf_img(file):
                    errores.append(f"Foto {i}: formato inválido (solo PNG, JPG, JPEG)")

        # Mostramos errores y no mostramos nada mas 
        if errores:
            return render_template('agregar_actividad.html', 
                                mensaje="Errores en el formulario", 
                                errores=errores,
                                regiones=regiones)

        # Convertir fechas a datetime
        from datetime import datetime
        try:
            inicio_dt = datetime.strptime(dia_hora_inicio, "%Y-%m-%dT%H:%M")
        except Exception:
            inicio_dt = None
        try:
            termino_dt = datetime.strptime(dia_hora_termino, "%Y-%m-%dT%H:%M")
        except Exception:
            termino_dt = None

        # Crear actividad
        actividad = db.create_actividad(
            comuna_id=comuna_id,
            sector=sector,
            nombre=nombre,
            email=email,
            celular=celular,
            dia_hora_inicio=inicio_dt,
            dia_hora_termino=termino_dt,
            descripcion=descripcion
        )

        actividad_id = actividad.id


        # Falta agregar la lógica para guardar fotos, temas y contactos (Implementado)

        #Guardar contactos
        contactos = [
            ("whatsapp", request.form.get("whatsapp-id")),
            ("instagram", request.form.get("instagram-id")),
            ("telegram", request.form.get("telegram-id")),
            ("x", request.form.get("x-id")),
            ("tiktok", request.form.get("tiktok-id")),
            ("otra", request.form.get("otra-id")),
        ]
        for nombre_contacto, identificador in contactos:
            if identificador and identificador.strip():
                db.create_contacto(nombre_contacto, identificador, actividad_id)

        # Guardar temas
        temas = [
            "música", "deporte", "ciencias", "religión", "política",
            "tecnología", "juegos", "baile", "comida", "otro"
        ]
        for tema in temas:
            if request.form.get(tema):
                db.create_tema(tema, None, actividad_id)
        # Tema "otro"
        if request.form.get("otro"):
            glosa_otro = escape(request.form.get("otro-id"))
            db.create_tema("otro", glosa_otro, actividad_id)

        # Guardar fotos
        for i in range(1, 6):
            file = request.files.get(f"foto{i}")
            if file and file.filename:
                filename = secure_filename(file.filename)
                ruta_archivo = os.path.join(app.config['UPLOAD_FOLDER'], filename)
                file.save(ruta_archivo)
                db.create_foto(
                    ruta_archivo=f"uploads/{filename}",
                    nombre_archivo=filename,
                    actividad_id=actividad_id
                )


        mensaje = "Actividad agregada exitosamente."
        return render_template('agregar_actividad.html', mensaje=mensaje, regiones=regiones)

    return render_template('agregar_actividad.html', mensaje=mensaje, regiones=regiones)

@app.route("/get-stats-data", methods=["GET"])
@cross_origin(origin="127.0.0.1", supports_credentials=True)
def get_estadisticas_data():
    #Obtener los datos para cada grafico
    actividades_dia = db.get_actividades_por_dia()
    actividades_tipo = db.get_actividades_por_tipo()
    actividades_horario_mes = db.get_actividades_por_horario_mes()

    datos_grafico_lineas = {
        "labels": [str(act.fecha) for act in actividades_dia],
        "datos": [act.cantidad for act in actividades_dia]
    }

    datos_grafico_torta = {
        "labels": [act.tema for act in actividades_tipo],
        "datos": [act.cantidad for act in actividades_tipo]
    }

    #Clasificar datos segun horario 
    meses = {i: {"mañana": 0, "mediodia": 0, "tarde":0} for i in range(1,13)}
    
    for act in actividades_horario_mes:
        mes = act.mes
        hora = act.hora
        if 6 <= hora < 12:
            meses[mes]["mañana"] += act.cantidad
        elif 12 <= hora < 14:
            meses[mes]["mediodia"] += act.cantidad
        elif 14 <= hora < 20:
            meses[mes]["tarde"] += act.cantidad
    
    nombres_meses = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", 
                    "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]
    
    datos_grafico_barras = {
        "labels": nombres_meses,
        "mañana": [meses[i+1]["mañana"] for i in range(12)],
        "mediodia": [meses[i+1]["mediodia"] for i in range(12)],
        "tarde": [meses[i+1]["tarde"] for i in range(12)]
    }

    return jsonify({
        "por_dia": datos_grafico_lineas,
        "por_tipo": datos_grafico_torta,
        "por_horario": datos_grafico_barras
    })

if __name__ == '__main__':
    app.run(debug=True)


