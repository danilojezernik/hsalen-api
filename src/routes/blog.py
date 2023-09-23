from fastapi import APIRouter, HTTPException

from src.database import db
from src.domain.blog import Blog

router = APIRouter()


# GET ALL BLOG
@router.get("/", operation_id="get_all_blogs")
async def get_all() -> list[Blog]:
    cursor = db.proces.blog.find()
    return [Blog(**document) for document in cursor]


# Get by ID
@router.get("/{_id}", operation_id="get_blog_by_id")
async def get_blog_id(_id: str):
    cursor = db.proces.blog.find_one({'_id': _id})
    if cursor is None:
        return HTTPException(status_code=400, detail=f"Blog by ID:{_id} does not exist")
    else:
        return Blog(**cursor)


# ADD BLOG
@router.post("/", operation_id="add_blog")
async def post_one(blog: Blog) -> Blog | None:
    blog_dict = blog.dict(by_alias=True)
    insert_result = db.proces.blog.insert_one(blog_dict)
    if insert_result.acknowledged:
        blog_dict['_id'] = str(insert_result.inserted_id)
        return Blog(**blog_dict)
    return None


# Edit by ID
@router.put("/{_id}", operation_id="edit_blog")
async def edit_blog(_id: str, blog: Blog) -> Blog | None:
    blog = blog.dict(by_alias=True)
    del blog['_id']

    cursor = db.proces.blog.update_one({'_id': _id}, {'$set': blog})
    if cursor.modified_count > 0:
        updated_document = db.proces.blog.find_one({'_id': _id})
        if updated_document:
            updated_document['_id'] = str(updated_document['_id'])
            return Blog(**updated_document)
    return None


# Delete by ID
@router.delete("/{_id}", operation_id="delete_blog")
async def delete_blog(_id: str) -> dict:
    delete_result = db.proces.blog.delete_one({'_id': _id})
    if delete_result.deleted_count > 0:
        return {"message": "Blog deleted successfully"}
    else:
        return {"message": "Blog not found"}
