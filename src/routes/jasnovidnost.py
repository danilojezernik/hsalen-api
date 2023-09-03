import json
from typing import List

from bson.json_util import dumps
from flask_openapi3 import APIBlueprint

from src.database import db
from src.domain.jasnovidnost import Jasnovidnost
from src.operation_id import operation_id_callback

jasnovidnost_bp = APIBlueprint('jasnovidnost', __name__, operation_id_callback=operation_id_callback)


@jasnovidnost_bp.get('/api/jasnovidnost', responses={200: Jasnovidnost})
def get_jasnovidnost() -> List[Jasnovidnost]:
    jasnovidnost = dumps(db.proces.jasnovidnost.find())
    return json.loads(jasnovidnost)
