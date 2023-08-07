import json
from bson.json_util import dumps

from bson import ObjectId
from flask import Blueprint, jsonify, request

from src.database import db

blog_bp = Blueprint("blog", __name__)


# PRIDOBI VSE OBJAVE
@blog_bp.route("/api/blog", methods=['GET'])
def get_blog():
    blog = dumps(db.proces.blog.find())
    return json.loads(blog)


# PRIDOBI OBJAVO PO ID
@blog_bp.route("/api/blog/<_id>", methods=['GET', 'POST'])
def get_blog_id(_id):
    blog_id = dumps(db.proces.blog.find_one({'_id': ObjectId(_id)}))
    return json.loads(blog_id)


# DODAJ NOVO OBJAVO
@blog_bp.route("/api/blog", methods=['POST'])
def post_blog():
    data = request.get_json()
    if data is not None:
        db.proces.blog.insert_one(data)
        return jsonify({'message': 'Objava uspešno dodana'})


# UREDI OBJAVO
@blog_bp.route("/api/blog/<int:id>", methods=['POST'])
def edit_blog(id):
    return jsonify({'stran': f'BLOG z metodo POST: Uredi objavo {id}'})


# IZBRIŠI OBJAVO
@blog_bp.route("/api/blog/<int:id>", methods=['DELETE'])
def delete_blog(id):
    return jsonify({'stran': f'BLOG z metodo DELETE: Izbriši objavo {id}'})
