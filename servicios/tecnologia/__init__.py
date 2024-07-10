from flask import Blueprint, request, redirect, url_for
from data import servicios

tecnologia_bp = Blueprint('tecnologia', __name__, url_prefix='/tecnologia')

@tecnologia_bp.route('/agregar', methods=['POST'])
def agregar():
    cliente = request.form['cliente']
    if cliente:
        servicios['tecnologia'].append(cliente)
    return redirect(url_for('index'))

@tecnologia_bp.route('/atender', methods=['GET'])
def atender():
    if servicios['tecnologia']:
        servicios['tecnologia'].pop(0)
    return redirect(url_for('index'))

