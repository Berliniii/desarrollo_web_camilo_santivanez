from flask import Flask, request, render_template
from utils.validations import validate_fechas
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

@app.route('/', methods=["GET", "POST"])
def index():
    return render_template('index.html')

@app.route('/listado')
def listado():
    return render_template('listado.html')

@app.route('/estadisticas')
def estadisticas():
    return render_template('estadisticas.html')

@app.route('/agregar_actividad')
def agregar():
    return render_template('agregar_actividad.html')

if __name__ == '__main__':
    app.run(debug=True)


