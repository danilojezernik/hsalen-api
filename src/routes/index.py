from flask import Blueprint, jsonify

index_bp = Blueprint("index", __name__)


@index_bp.route("/api/index", methods=['GET'])
def get_index():
    return jsonify({'stran': 'INDEX'})
