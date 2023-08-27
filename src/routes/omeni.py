import json

from bson.json_util import dumps
from flask_openapi3 import APIBlueprint

from src.database import db
from src.operation_id import operation_id_callback

omeni_bp = APIBlueprint('omeni', __name__, operation_id_callback=operation_id_callback)


@omeni_bp.get('/api/omeni')
def get_omeni():
    omeni = dumps(db.proces.jaz.find())
    return json.loads(omeni)


@omeni_bp.get('/api/mediji')
def get_mediji():
    mediji = dumps(db.proces.mediji.find())
    return json.loads(mediji)


