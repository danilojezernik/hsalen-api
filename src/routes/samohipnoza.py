import json
from typing import List

from bson.json_util import dumps
from flask_openapi3 import APIBlueprint

from src.database import db
from src.domain.samohipnoza import Samohipnoza
from src.operation_id import operation_id_callback

samohipnoza_bp = APIBlueprint('samohipnoza', __name__, operation_id_callback=operation_id_callback)


@samohipnoza_bp.get('/api/samohipnoza', responses={200: Samohipnoza})
def get_samohipnoza() -> List[Samohipnoza]:
    samohipnoza = dumps(db.proces.samohipnoza.find())
    return json.loads(samohipnoza)
