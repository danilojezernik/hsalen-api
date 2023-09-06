from fastapi import APIRouter

from src.database import db
from src.domain.jasnovidnost import Jasnovidnost

router = APIRouter()


@router.get('/')
async def get_jasnovidnost() -> list[Jasnovidnost]:
    cursor = db.proces.jasnovidnost.find()
    return [Jasnovidnost(**document) for document in cursor]
