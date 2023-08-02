from flask import Blueprint, jsonify

regresija_bp = Blueprint('regresija', __name__)


@regresija_bp.route('/api/regresija')
def get_regresija():
    return jsonify({'stran': 'REGRESIJA'})
