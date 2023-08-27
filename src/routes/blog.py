import json
from bson.json_util import dumps

from bson import ObjectId
from flask import jsonify, request
from flask_jwt_extended import jwt_required
from flask_openapi3 import APIBlueprint

from src.database import db

blog_bp = APIBlueprint("blog", __name__)


# Get all blog
@blog_bp.get("/api/blog")
def get_blog():
    blog = dumps(db.proces.blog.find())
    return json.loads(blog)


# Update blog
@blog_bp.post("/api/blog")
@jwt_required()
def post_blog():
    data = request.get_json()
    if data is not None:
        db.proces.blog.insert_one(data)
        return jsonify({'message': 'Objava uspešno dodana'})


# Get by ID
@blog_bp.get("/api/blog/<_id>")
def get_blog_id(_id):
    blog_id = dumps(db.proces.blog.find_one({'_id': ObjectId(_id)}))
    return json.loads(blog_id)


# POST by ID
@blog_bp.post("/api/blog/<_id>")
def post_blog_id(_id):
    blog_id = dumps(db.proces.blog.find_one({'_id': ObjectId(_id)}))
    return json.loads(blog_id)


# Edit by ID
@blog_bp.post("/api/blog/edit/<_id>")
@jwt_required()
def edit_blog(_id):
    data = request.get_json()

    if '_id' in data:
        del data['_id']

    result = db.proces.blog.update_one({'_id': ObjectId(_id)}, {'$set': data})
    if result.modified_count > 0:
        updated_document = db.proces.blog.find_one({'_id': ObjectId(_id)})
        updated_document['_id'] = str(updated_document['_id'])
        return jsonify({"message": "Objava uspešno posodobljena", "updated_document": updated_document})
    else:
        return jsonify({"error": "Objava bloga ni uspela!"})


# Delete by ID
@blog_bp.delete("/api/blog/delete/<_id>")
@jwt_required()
def delete_blog(_id):
    try:
        result = db.proces.blog.delete_one({'_id': ObjectId(_id)})
        if result.deleted_count > 0:
            return jsonify({'message': 'Blog deleted'}), 200
        else:
            return jsonify({'error': 'Blog not found'}), 404
    except Exception as e:
        return jsonify({'error': str(e)}), 500
