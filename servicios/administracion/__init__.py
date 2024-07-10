from flask import Blueprint, request, redirect, url_for
from data import servicios

administracion_bp = Blueprint('administracion', __name__, url_prefix='/administracion')

@administracion_bp.route('/agregar', methods=['POST'])
def agregar():
    cliente = request.form['cliente']
    if cliente:
        servicios['administracion'].append(cliente)
    return redirect(url_for('index'))

@administracion_bp.route('/atender', methods=['GET'])
def atender():
    if servicios['administracion']:
        servicios['administracion'].pop(0)
    return redirect(url_for('index'))

