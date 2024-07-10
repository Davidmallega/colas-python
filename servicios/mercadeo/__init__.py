from flask import Blueprint, request, redirect, url_for
from data import servicios

mercadeo_bp = Blueprint('mercadeo', __name__, url_prefix='/mercadeo')

@mercadeo_bp.route('/agregar', methods=['POST'])
def agregar():
    cliente = request.form['cliente']
    if cliente:
        servicios['mercadeo'].append(cliente)
    return redirect(url_for('index'))

@mercadeo_bp.route('/atender', methods=['GET'])
def atender():
    if servicios['mercadeo']:
        servicios['mercadeo'].pop(0)
    return redirect(url_for('index'))
