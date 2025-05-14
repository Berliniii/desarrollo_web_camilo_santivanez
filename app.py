from flask import Flask, request, render_template, url_for, session, redirect
from utils.validations import *
from database import db
from werkzeug.utils import secure_filename
import hashlib
import filetype
import os

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
    return render_template('listado.html')

@app.route('/estadisticas')
def estadisticas():
    return render_template('estadisticas.html')

@app.route('/agregar_actividad', methods=["GET", "POST"])
def agregar():
    mensaje = None
    if request.method == "POST":
        # Obtener datos del formulario
        comuna_id = request.form.get("select-comuna")
        sector = request.form.get("sector")
        nombre = request.form.get("nombre_organizador")
        email = request.form.get("email-organizador")
        celular = request.form.get("celu-organizador")
        dia_hora_inicio = request.form.get("dia-hora-inicio")
        dia_hora_termino = request.form.get("dia-hora-termino")
        descripcion = request.form.get("descripcion-actividad")

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

        # Falta agregar la lógica para guardar fotos, temas y contactos 

        mensaje = "Actividad agregada exitosamente."

    return render_template('agregar_actividad.html', mensaje=mensaje)

if __name__ == '__main__':
    app.run(debug=True)


