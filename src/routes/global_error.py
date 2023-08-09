import json

from bson import ObjectId
from bson.json_util import dumps

from flask import Blueprint, jsonify, request

from src.database import db

global_error_bp = Blueprint("global_error", __name__)


# PRIDOBI VSE ERROR-je
@global_error_bp.route("/api/error", methods=['GET'])
def get_error():
    blog = dumps(db.proces.error.find())
    return json.loads(blog)


@global_error_bp.route('/api/error/<_id>', methods=['GET', 'POST'])
def get_error_id(_id):
    error = dumps(db.proces.error.find_one({'_id': ObjectId(_id)}))
    return json.loads(error)


# DODAJ NOV ERROR
@global_error_bp.route("/api/error", methods=['POST'])
def post_blog():
    data = request.get_json()
    print(data)
    if data is not None:
        db.proces.error.insert_one(data)
        return jsonify({'message': 'Objava uspešno dodana'})


@global_error_bp.route('/api/error/delete', methods=['DELETE'])
def delete_all_errors():
    db.proces.error.delete_many({})
    return jsonify({"message": "Vsi error-ji izbrisani uspešno"})


@global_error_bp.route('/api/error/delete/<_id>', methods=['DELETE'])
def delete_error_by_id(_id):
    db.proces.error.delete_one({'_id': ObjectId(_id)})
    return jsonify({"message": f"Blog _${_id}_ izbrisan uspešno!"})
