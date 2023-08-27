import json

from bson.json_util import dumps
from flask_openapi3 import APIBlueprint

from src.database import db

samohipnoza_bp = APIBlueprint('samohipnoza', __name__)


@samohipnoza_bp.get('/api/samohipnoza')
def get_samohipnoza():
    samohipnoza = dumps(db.proces.samohipnoza.find())
    return json.loads(samohipnoza)
