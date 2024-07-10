import sys
import os
from flask import Flask, render_template, request, redirect, url_for

# Asegurar que el directorio de servicios esté en el sys.path
servicios_path = os.path.abspath(os.path.join(os.path.dirname(__file__), 'servicios'))
sys.path.append(servicios_path)

# Imprimir el sys.path para depuración
print("sys.path:", sys.path)

# Importar los Blueprints de cada servicio
from servicios.servicios_generales import servicios_generales_bp
from servicios.administracion import administracion_bp
from servicios.facturacion import facturacion_bp
from servicios.tecnologia import tecnologia_bp
from servicios.mercadeo import mercadeo_bp
from data import servicios

app = Flask(__name__)

# Registrar los Blueprints
app.register_blueprint(servicios_generales_bp)
app.register_blueprint(administracion_bp)
app.register_blueprint(facturacion_bp)
app.register_blueprint(tecnologia_bp)
app.register_blueprint(mercadeo_bp)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/colas')
def colas():
    return render_template('colas.html', servicios=servicios)

@app.route('/registrar_cliente', methods=['POST'])
def registrar_cliente():
    cliente = request.form['cliente']
    servicio = request.form['servicio']
    if cliente and servicio in servicios:
        servicios[servicio].append(cliente)
    return redirect(url_for('colas'))

if __name__ == '__main__':
    app.run(debug=True)
