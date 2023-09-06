from fastapi import APIRouter

from src.database import db
from src.domain.hipnoterapija import Hipnoterapija

router = APIRouter()


@router.get("/")
def get_hipnoterapija() -> list[Hipnoterapija]:
    cursor = db.proces.hipnoterapija.find()
    return [Hipnoterapija(**document) for document in cursor]
