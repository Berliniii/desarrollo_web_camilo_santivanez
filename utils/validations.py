import re
import filetype
from datetime import datetime

def validate_region(value):
    return value

def validate_comuna(value):
    return value 

def validate_sector(value):
    return value.strip() == "" or len(value) <= 100

def validate_nombre(value):
    return value and len(value) <= 200

def validate_email(value):
    regex = r'^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,7}$'
    return value and re.fullmatch(regex, value)

def validate_celular(value):
    is_empty = value.strip() == ""
    is_valid_format = re.fullmatch(r'^\+569\.\d{8}$', value) is not None
    return is_empty or is_valid_format

# --- Por implementar ---
# contacto, tema (no se me ocurre como hacerlo :c)

def validate_fechas(fecha_inicio, fecha_termino):
    try:
        fecha_inicio = datetime.fromisoformat(fecha_inicio)
    except ValueError:
        return False  # formato inválido en fecha de inicio

    # Fecha de término vacía es válida
    if not fecha_termino or fecha_termino.strip() == "":
        return True

    try:
        fecha_termino = datetime.fromisoformat(fecha_termino)
    except ValueError:
        return False  # formato inválido en fecha de término

    # La fecha de término debe ser mayor que la de inicio
    return fecha_termino > fecha_inicio

def validate_conf_img(conf_img):
    ALLOWED_EXTENSIONS = {"png", "jpg", "jpeg", "gif"}
    ALLOWED_MIMETYPES = {"image/jpeg", "image/png", "image/gif"}

    # check if a file was submitted
    if conf_img is None:
        return False

    # check if the browser submitted an empty file
    if conf_img.filename == "":
        return False
    
    # check file extension
    ftype_guess = filetype.guess(conf_img)
    if ftype_guess.extension not in ALLOWED_EXTENSIONS:
        return False
    # check mimetype
    if ftype_guess.mime not in ALLOWED_MIMETYPES:
        return False
    return True