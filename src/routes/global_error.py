import json
from bson.json_util import dumps

from flask import Blueprint, jsonify, request

from src.database import db

global_error_bp = Blueprint("global_error", __name__)


# PRIDOBI VSE ERROR-je
@global_error_bp.route("/api/error", methods=['GET'])
def get_error():
    blog = dumps(db.proces.error.find())
    return json.loads(blog)


# DODAJ NOV ERROR
@global_error_bp.route("/api/error", methods=['POST'])
def post_blog():
    data = request.get_json()
    print(data)
    if data is not None:
        db.proces.error.insert_one(data)
        return jsonify({'message': 'Objava uspešno dodana'})
