import json

from bson.json_util import dumps
from flask import Blueprint, jsonify

from src.database import db

samohipnoza_bp = Blueprint('samohipnoza', __name__)


@samohipnoza_bp.route('/api/samohipnoza')
def get_samohipnoza():
    samohipnoza = dumps(db.proces.samohipnoza.find())
    return json.loads(samohipnoza)
