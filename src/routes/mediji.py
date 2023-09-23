from fastapi import APIRouter, HTTPException

from src.database import db
from src.domain.mediji import Mediji

router = APIRouter()


# GET ALL MEDIJI
@router.get('/', operation_id="get_all_mediji")
def get_mediji() -> list[Mediji]:
    cursor = db.proces.mediji.find()
    return [Mediji(**document) for document in cursor]


# GET MEDIJI BY ID
@router.get("/{_id}", operation_id="get_blog_by_id")
async def get_mediji_id(_id: str):
    cursor = db.proces.mediji.find_one({'_id': _id})
    if cursor is None:
        return HTTPException(status_code=400, detail=f"Mediji by ID:{_id} does not exist")
    else:
        return Mediji(**cursor)


# ADD MEDIJI
@router.post("/", operation_id="add_mediji")
async def post_one(mediji: Mediji) -> Mediji | None:
    mediji_dict = mediji.dict(by_alias=True)
    insert_result = db.proces.blog.insert_one(mediji_dict)
    if insert_result.acknowledged:
        mediji_dict['_id'] = str(insert_result.inserted_id)
        return Mediji(**mediji_dict)
    return None


# EDIT MEDIJI
@router.post("/edit/{_id}", operation_id="edit_mediji")
async def edit_blog(_id: str, mediji: Mediji) -> Mediji:
    if '_id' in mediji:
        mediji = mediji.dict()
        del mediji['_id']

    cursor = db.proces.mediji.update_one({'_id': _id}, {'$set': mediji})
    if cursor.modified_count > 0:
        updated_document = db.proces.mediji.find_one({'_id': _id})
        updated_document['_id'] = str(updated_document['_id'])

    return Mediji(**cursor)


# DELETE MEDIJI
@router.delete("/{_id}", operation_id="delete_mediji")
async def delete_blog(_id: str) -> Mediji:
    cursor = db.proces.mediji.delete_one({'_id': _id})
    return Mediji(**cursor)
