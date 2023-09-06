from fastapi import APIRouter

from src.database import db
from src.domain.global_error import GlobalError

router = APIRouter()


@router.get("/")
async def get_error() -> list[GlobalError]:
    cursor = db.proces.error.find()
    return [GlobalError(**document) for document in cursor]


@router.post('/{_id}')
async def post_error_id(_id: str) -> GlobalError:
    cursor = db.proces.error.find_one({'_id': _id})
    return GlobalError(**cursor)


@router.get('/{_id}')
async def get_error_id(_id: str) -> GlobalError:
    cursor = db.proces.error.find_one({'_id': _id})
    return GlobalError(**cursor)


@router.post("/")
async def post_error(error: GlobalError) -> GlobalError:
    cursor = db.proces.error.insert_one(error)
    return GlobalError(**cursor)


@router.delete('/')
async def delete_all_errors() -> list[GlobalError]:
    cursor = db.proces.error.delete_many({})
    return [GlobalError(**document) for document in cursor]


@router.delete('/{_id}')
def delete_error_by_id(_id: str) -> GlobalError:
    cursor = db.proces.error.delete_one({'_id': _id})
    return GlobalError(**cursor)
