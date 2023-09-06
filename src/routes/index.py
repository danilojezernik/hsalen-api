from fastapi import APIRouter

from src.database import db
from src.domain.index import Index
from src.domain.knjiga import Knjiga

router = APIRouter()


@router.get("/api/index")
def get_index() -> list[Index]:
    cursor = db.proces.index.find()
    return [Index(**document) for document in cursor]


@router.get("/api/index/knjiga")
def get_knjiga() -> list[Knjiga]:
    cursor = db.proces.knjiga.find()
    return [Knjiga(**document) for document in cursor]
