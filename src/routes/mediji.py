from fastapi import APIRouter, HTTPException

from src.services import db
from src.domain.mediji import Mediji

router = APIRouter()


# GET ALL MEDIJI
@router.get('/', operation_id="get_all_mediji")
def get_mediji() -> list[Mediji]:
    cursor = db.proces.mediji.find()
    return [Mediji(**document) for document in cursor]


# GET MEDIJI BY ID
@router.get("/{_id}", operation_id="get_mediji_by_id")
async def get_mediji_id(_id: str):
    cursor = db.proces.mediji.find_one({'_id': _id})
    if cursor is None:
        return HTTPException(status_code=404, detail=f"Mediji by ID:{_id} does not exist")
    else:
        return Mediji(**cursor)


# ADD MEDIJI
@router.post("/", operation_id="add_mediji")
async def post_one(mediji: Mediji) -> Mediji | None:
    mediji_dict = mediji.dict(by_alias=True)
    insert_result = db.proces.mediji.insert_one(mediji_dict)
    if insert_result.acknowledged:
        mediji_dict['_id'] = str(insert_result.inserted_id)
        return Mediji(**mediji_dict)
    return None


# EDIT MEDIJI
@router.put("/{_id}", operation_id="edit_mediji")
async def edit_mediji(_id: str, mediji: Mediji) -> Mediji | None:
    mediji = mediji.dict(by_alias=True)
    del mediji['_id']

    cursor = db.proces.mediji.update_one({'_id': _id}, {'$set': mediji})
    if cursor.modified_count > 0:
        updated_document = db.proces.mediji.find_one({'_id': _id})
        if updated_document:
            updated_document['_id'] = str(updated_document['_id'])
            return Mediji(**updated_document)
    return None


# DELETE MEDIJI
@router.delete("/{_id}", operation_id="delete_mediji")
async def delete_mediji(_id: str):
    delete_result = db.proces.mediji.delete_one({'_id': _id})
    if delete_result.deleted_count > 0:
        return {"message": f"Mediji with id:({_id}) deleted successfully"}
    else:
        return HTTPException(status_code=404, detail=f"Mediji by ID:({_id}) not found")

