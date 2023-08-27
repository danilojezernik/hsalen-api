import json

from bson.json_util import dumps
from flask_openapi3 import APIBlueprint

from src.database import db
from src.operation_id import operation_id_callback

samohipnoza_bp = APIBlueprint('samohipnoza', __name__, operation_id_callback=operation_id_callback)


@samohipnoza_bp.get('/api/samohipnoza')
def get_samohipnoza():
    samohipnoza = dumps(db.proces.samohipnoza.find())
    return json.loads(samohipnoza)
