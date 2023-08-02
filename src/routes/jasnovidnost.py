from flask import Blueprint, jsonify

jasnovidnost_bp = Blueprint('jasnovidnost', __name__)


@jasnovidnost_bp.route('/api/jasnovidnost')
def get_jasnovidnost():
    return jsonify({'stran': 'JASNOVIDNOST'})
