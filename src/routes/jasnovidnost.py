import json

from bson.json_util import dumps
from flask_openapi3 import APIBlueprint

from src.database import db

jasnovidnost_bp = APIBlueprint('jasnovidnost', __name__)


@jasnovidnost_bp.get('/api/jasnovidnost')
def get_jasnovidnost():
    jasnovidnost = dumps(db.proces.jasnovidnost.find())
    return json.loads(jasnovidnost)
