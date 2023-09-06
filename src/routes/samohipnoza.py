from fastapi import APIRouter

from src.database import db
from src.domain.samohipnoza import Samohipnoza

router = APIRouter()


@router.get('/')
async def get_samohipnoza() -> list[Samohipnoza]:
    cursor = db.proces.samohipnoza.find()
    return [Samohipnoza(**document) for document in cursor]
