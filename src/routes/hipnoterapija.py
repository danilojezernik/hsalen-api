from flask import Blueprint, jsonify

hipnoterapija_bp = Blueprint("hipnoterapija", __name__)


@hipnoterapija_bp.route("/api/hipnoterapija", methods=['GET'])
def get_hipnoterapija():
    return jsonify({'stran': 'HIPNOTERAPIJA'})
