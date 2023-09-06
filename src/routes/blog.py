from fastapi import APIRouter

from src.database import db
from src.domain.blog import Blog

router = APIRouter()


# Get all blog
@router.get("/")
async def get_blog() -> list[Blog]:
    cursor = db.proces.blog.find()
    return [Blog(**document) for document in cursor]


# Update blog
@router.post("/")
async def post_blog(blog: Blog) -> Blog:
    cursor = db.proces.blog.insert_one(blog)
    return Blog(**cursor)


# Get by ID
@router.get("/{_id}")
async def get_blog_id(_id: str) -> Blog:
    cursor = db.proces.blog.find_one({'_id': _id})
    return Blog(**cursor)


# POST by ID
@router.post("/{_id}")
async def post_blog_id(_id: str) -> Blog:
    cursor = db.proces.blog.find_one({'_id': _id})
    return Blog(**cursor)


# Edit by ID
@router.post("/edit/{_id}")
async def edit_blog(_id: str, blog: Blog) -> Blog:

    if '_id' in blog:
        blog = blog.dict()
        del blog['_id']

    cursor = db.proces.blog.update_one({'_id': _id}, {'$set': blog})
    if cursor.modified_count > 0:
        updated_document = db.proces.blog.find_one({'_id': _id})
        updated_document['_id'] = str(updated_document['_id'])

    return Blog(**cursor)


# Delete by ID
@router.delete("/{_id}")
async def delete_blog(_id: str) -> Blog:
    cursor = db.proces.blog.delete_one({'_id': _id})
    return Blog(**cursor)
