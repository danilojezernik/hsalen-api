"""
This module defines API routes for managing blogs.

Routes:
1. GET all blogs
2. GET blog by ID
3. ADD a new blog
4. Edit an existing blog by ID
5. Delete a blog by ID
"""

from fastapi import APIRouter, HTTPException, Depends
from src.services import db
from src.domain.blog import Blog
from src.services.security import get_current_user

router = APIRouter()


# GET ALL BLOG
@router.get("/", operation_id="get_all_blogs")
async def get_all() -> list[Blog]:
    """
    This route handles the retrieval of all blogs from the database.

    Behavior:
    - Retrieves all blogs from the database.
    - Returns a list of Blog objects.
    """

    # Retrieve all blogs from the database
    cursor = db.proces.blog.find()
    return [Blog(**document) for document in cursor]


# Get by ID
@router.get("/{_id}", operation_id="get_blog_by_id")
async def get_blog_id(_id: str):
    """
    This route handles the retrieval of a blog by its ID from the database.

    Parameters:
    - _id (str): ID of the blog to retrieve.

    Behavior:
    - Retrieves a blog by its ID from the database.
    - Returns the Blog object if found, or raises an exception if not found.
    """

    # Retrieve a blog by its ID from the database
    cursor = db.proces.blog.find_one({'_id': _id})
    if cursor is None:
        raise HTTPException(status_code=400, detail=f"Blog by ID:{_id} does not exist")
    else:
        return Blog(**cursor)


@router.post("/", operation_id="add_blog")
async def post_one(blog: Blog, current_user: str = Depends(get_current_user)) -> Blog | None:
    """
    This route adds a new blog to the database.

    Parameters:
    - blog (Blog): The blog object to be added.
    - current_user (str): The username of the authenticated user.

    Behavior:
    - Adds a new blog to the database.
    - Returns the added Blog object if successful, or None if unsuccessful.
    """

    # Add a new blog to the database
    blog_dict = blog.dict(by_alias=True)
    insert_result = db.proces.blog.insert_one(blog_dict)
    if insert_result.acknowledged:
        blog_dict['_id'] = str(insert_result.inserted_id)
        return Blog(**blog_dict)
    return None


# Edit by ID
@router.put("/{_id}", operation_id="edit_blog")
async def edit_blog(_id: str, blog: Blog, current_user: str = Depends(get_current_user)) -> Blog | None:
    """
    This route edits an existing blog by its ID in the database.

    Parameters:
    - _id (str): The ID of the blog to be edited.
    - blog (Blog): The updated blog object.
    - current_user (str): The username of the authenticated user.

    Behavior:
    - Edits an existing blog by its ID in the database.
    - Returns the updated Blog object if successful, or None if unsuccessful.
    """

    # Edit an existing blog by its ID in the database
    blog = blog.dict(by_alias=True)
    del blog['_id']

    # Update the blog in the database
    cursor = db.proces.blog.update_one({'_id': _id}, {'$set': blog})

    # Check if the blog was successfully updated
    if cursor.modified_count > 0:
        # Retrieve the updated blog from the database
        updated_document = db.proces.blog.find_one({'_id': _id})

        # Check if the updated blog exists
        if updated_document:
            updated_document['_id'] = str(updated_document['_id'])
            return Blog(**updated_document)

    # Return None if the blog was not updated
    return None


# Delete a blog by its ID from the database
@router.delete("/{_id}", operation_id="delete_blog")
async def delete_blog(_id: str, current_user: str = Depends(get_current_user)):
    """
    Route to delete a blog by its ID from the database.

    Arguments:
        _id (str): The ID of the blog to be deleted.
        current_user (str): The current authenticated user.

    Returns:
        dict: A message indicating the status of the deletion.

    Raises:
        HTTPException: If the blog is not found for deletion.
    """

    # Attempt to delete the blog from the database
    delete_result = db.proces.blog.delete_one({'_id': _id})

    # Check if the blog was successfully deleted
    if delete_result.deleted_count > 0:
        return {"message": "Blog deleted successfully"}
    else:
        # Raise an exception if the blog was not found for deletion
        raise HTTPException(status_code=404, detail=f"Blog by ID:({_id}) not found")
