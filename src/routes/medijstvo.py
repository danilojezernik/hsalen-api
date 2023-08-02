from flask import Blueprint, jsonify

medijstvo_bp = Blueprint('medijstvo', __name__)


@medijstvo_bp.route('/api/medijstvo')
def get_medijstvo():
    return jsonify({'stran': 'MEDIJSTVO'})
