from flask import Blueprint, request, redirect, url_for
from data import servicios

facturacion_bp = Blueprint('facturacion', __name__, url_prefix='/facturacion')

@facturacion_bp.route('/agregar', methods=['POST'])
def agregar():
    cliente = request.form['cliente']
    if cliente:
        servicios['facturacion'].append(cliente)
    return redirect(url_for('index'))

@facturacion_bp.route('/atender', methods=['GET'])
def atender():
    if servicios['facturacion']:
        servicios['facturacion'].pop(0)
    return redirect(url_for('index'))
