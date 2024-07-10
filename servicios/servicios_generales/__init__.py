from flask import Blueprint, request, redirect, url_for
from data import servicios

servicios_generales_bp = Blueprint('servicios_generales', __name__, url_prefix='/servicios_generales')

@servicios_generales_bp.route('/agregar', methods=['POST'])
def agregar():
    cliente = request.form['cliente']
    if cliente:
        servicios['servicios_generales'].append(cliente)
    return redirect(url_for('index'))

@servicios_generales_bp.route('/atender', methods=['GET'])
def atender():
    if servicios['servicios_generales']:
        servicios['servicios_generales'].pop(0)
    return redirect(url_for('index'))

@servicios_generales_bp.route('/registrar_cliente', methods=['POST'])
def registrar_cliente():
    cliente = request.form['cliente']
    if cliente:
        servicios['servicios_generales'].append(cliente)
    return redirect(url_for('index'))
