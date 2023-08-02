from json import dumps

from bson import ObjectId
from flask import Blueprint, jsonify

blog_bp = Blueprint("blog", __name__)


# PRIDOBI VSE OBJAVE
@blog_bp.route("/api/blog", methods=['GET'])
def get_blog():
    return jsonify({'stran': 'BLOG'})


# PRIDOBI OBJAVO PO ID
@blog_bp.route("/api/blog/<int:id>", methods=['GET'])
def get_blog_id(id):
    return jsonify({'stran': f'BLOG by {id}'})


# DODAJ NOVO OBJAVO
@blog_bp.route("/api/blog", methods=['POST'])
def post_blog():
    return jsonify({'stran': 'BLOG z metodo POST: Dodaj novo objavo'})


# UREDI OBJAVO
@blog_bp.route("/api/blog/<int:id>", methods=['POST'])
def edit_blog(id):
    return jsonify({'stran': f'BLOG z metodo POST: Uredi objavo {id}'})


# IZBRIŠI OBJAVO
@blog_bp.route("/api/blog/<int:id>", methods=['DELETE'])
def delete_blog(id):
    return jsonify({'stran': f'BLOG z metodo DELETE: Izbriši objavo {id}'})
