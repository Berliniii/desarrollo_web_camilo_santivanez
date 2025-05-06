from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('html/index.html')

@app.route('/listado')
def listado():
    return render_template('html/listado.html')

@app.route('/estadisticas')
def estadisticas():
    return render_template('html/estadisticas.html')

@app.route('/agregar_actividad')
def agregar():
    return render_template('html/agregar_actividad.html')
if __name__ == '__main__':
    app.run(debug=True)


