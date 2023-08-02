from flask import Blueprint, jsonify

omeni_bp = Blueprint('omeni', __name__)


@omeni_bp.route('/api/omeni')
def get_omeni():
    return jsonify({'stran': 'O MENI'})
