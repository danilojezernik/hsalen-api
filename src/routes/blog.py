"""
This module defines API routes for managing blogs.

Routes:
1. GET all blogs
2. GET blog by ID
3. ADD a new blog
4. Edit an existing blog by ID
5. Delete a blog by ID
"""
import datetime

# Import necessary modules and classes
from fastapi import APIRouter, HTTPException, Depends, status, Request

from src.services import db
from src.domain.blog import Blog
from src.services.security import get_current_user

# Logging
from src.domain.logging import Logging
from src.services.db_logging import proces_log

# Create a router for handling Mediji related endpoints
router = APIRouter()


# GET ALL BLOG
@router.get("/", operation_id="get_all_blogs")
async def get_all(request: Request) -> list[Blog]:
    """
    This route handles the retrieval of all blogs from the database.

    Behavior:
    - Retrieves all blogs from the database.
    - Returns a list of Blog objects.
    """

    # Get the path and method of the current route and client host from the request
    route_path = request.url.path
    route_method = request.method
    client_host = request.client.host

    try:
        # Save route path to logging collection
        log_entry = Logging(
            route_action=route_path,
            method=route_method,
            client_host=client_host,
            content='Request made to: GET ALL BLOGS - PUBLIC',
            status_code=status.HTTP_200_OK,
            datum_vnosa=datetime.datetime.now()
        )
        proces_log.logging.insert_one(log_entry.dict(by_alias=True))

        # Retrieve all blogs from the database
        cursor = db.proces.blog.find()
        return [Blog(**document) for document in cursor]

    except Exception as e:
        # Log the exception
        error_log_entry = Logging(
            route_action=route_path,
            method=route_method,
            client_host=client_host,
            content=f'An error occurred: {str(e)}',
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            datum_vnosa=datetime.datetime.now()
        )
        proces_log.logging.insert_one(error_log_entry.dict(by_alias=True))

        # Raise an HTTPException with a 500 Internal Server Error status code
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail='Internal Server Error'
        )


# GET ALL BLOG LIMIT 4
@router.get("/limited", operation_id="get_limited_blogs")
async def get_limited_blogs(request: Request) -> list[Blog]:
    """
    This route handles the retrieval of limited amount of blogs from the database.

    Behavior:
    - Retrieves limited amount of blogs from the database.
    - Returns a limited list of Blog objects.
    """

    # Get the path of the current route from the request
    route_path = request.url.path
    route_method = request.method
    client_host = request.client.host

    try:
        # Save route path to logging collection
        log_entry = Logging(
            route_action=route_path,
            method=route_method,
            client_host=client_host,
            content='Request made to: GET ALL BLOG LIMIT 4 - PUBLIC',
            status_code=status.HTTP_200_OK,
            datum_vnosa=datetime.datetime.now()
        )
        proces_log.logging.insert_one(log_entry.dict(by_alias=True))

        # Retrieve limited amount of blogs from the database
        cursor = db.proces.blog.find().limit(4)
        return [Blog(**document) for document in cursor]

    except Exception as e:
        # Log the exception
        error_log_entry = Logging(
            route_action=route_path,
            method=route_method,
            client_host=client_host,
            content=f'An error occurred: {str(e)}',
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            datum_vnosa=datetime.datetime.now()
        )
        proces_log.logging.insert_one(error_log_entry.dict(by_alias=True))

        # Raise an HTTPException with a 500 Internal Server Error status code
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail='Internal Server Error'
        )


# Get by ID
@router.get("/{_id}", operation_id="get_blog_by_id")
async def get_blog_id(request: Request, _id: str):
    """
    This route handles the retrieval of a blog by its ID from the database.

    Parameters:
    - _id (str): ID of the blog to retrieve.

    Behavior:
    - Retrieves a blog by its ID from the database.
    - Returns the Blog object if found, or raises an exception if not found.
    """

    # Get the path of the current route from the request
    route_path = request.url.path
    route_method = request.method
    client_host = request.client.host

    try:
        # Save route path to logging collection
        log_entry = Logging(
            route_action=route_path,
            method=route_method,
            client_host=client_host,
            content='Request made to: GET BLOG BY ID - PUBLIC',
            status_code=status.HTTP_200_OK,
            datum_vnosa=datetime.datetime.now()
        )
        proces_log.logging.insert_one(log_entry.dict(by_alias=True))

        # Retrieve a blog by its ID from the database
        cursor = db.proces.blog.find_one({'_id': _id})
        if cursor is None:
            raise HTTPException(status_code=404, detail=f"Blog by ID:{_id} does not exist")
        else:
            return Blog(**cursor)

    except Exception as e:
        # Log the exception
        error_log_entry = Logging(
            route_action=route_path,
            method=route_method,
            client_host=client_host,
            content=f'An error occurred: {str(e)}',
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            datum_vnosa=datetime.datetime.now()
        )
        proces_log.logging.insert_one(error_log_entry.dict(by_alias=True))

        # Raise an HTTPException with a 500 Internal Server Error status code
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail='Internal Server Error'
        )


# ADMIN

# Get all BLOG for ADMIN
@router.get("/admin/", operation_id="get_all_blogs_admin")
async def get_all_admin(request: Request, current_user: str = Depends(get_current_user)) -> list[Blog]:
    """
    This route handles the retrieval of all blogs from the database.

    Behavior:
    - Retrieves all blogs from the database.
    - Returns a list of Blog objects.
    """

    # Get the path of the current route from the request
    route_path = request.url.path
    route_method = request.method
    client_host = request.client.host

    try:
        # Save route path to logging collection
        log_entry = Logging(
            route_action=route_path,
            method=route_method,
            client_host=client_host,
            content='Request made to: GET ALL BLOGS - PRIVATE',
            status_code=status.HTTP_200_OK,
            datum_vnosa=datetime.datetime.now()
        )
        proces_log.logging.insert_one(log_entry.dict(by_alias=True))

        # Retrieve all blogs from the database for ADMIN
        cursor = db.proces.blog.find()
        return [Blog(**document) for document in cursor]

    except Exception as e:
        # Log the exception
        error_log_entry = Logging(
            route_action=route_path,
            method=route_method,
            client_host=client_host,
            content=f'An error occurred: {str(e)}',
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            datum_vnosa=datetime.datetime.now()
        )
        proces_log.logging.insert_one(error_log_entry.dict(by_alias=True))

        # Raise an HTTPException with a 500 Internal Server Error status code
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail='Internal Server Error'
        )


# Get by ID for Admin
@router.get("/admin/{_id}", operation_id="get_blog_by_id_admin")
async def get_blog_id_admin(request: Request, _id: str, current_user: str = Depends(get_current_user)):
    """
    This route handles the retrieval of a blog by its ID from the database.

    Parameters:
    - _id (str): ID of the blog to retrieve.

    Behavior:
    - Retrieves a blog by its ID from the database.
    - Returns the Blog object if found, or raises an exception if not found.
    """

    # Get the path of the current route from the request
    route_path = request.url.path
    route_method = request.method
    client_host = request.client.host

    try:
        # Save route path to logging collection
        log_entry = Logging(
            route_action=route_path,
            method=route_method,
            client_host=client_host,
            content=f'Request made to: GET BLOG BY ID - PRIVATE, ID: {_id}',
            status_code=status.HTTP_200_OK,
            datum_vnosa=datetime.datetime.now()
        )
        proces_log.logging.insert_one(log_entry.dict(by_alias=True))

        # Retrieve a blog by its ID from the database
        cursor = db.proces.blog.find_one({'_id': _id})
        if cursor is None:
            # Log the error and raise HTTPException for 404
            error_log_entry = Logging(
                route_action=route_path,
                method=route_method,
                client_host=client_host,
                content=f'Blog with ID {_id} not found - PRIVATE',
                status_code=status.HTTP_404_NOT_FOUND,
                datum_vnosa=datetime.datetime.now()
            )
            proces_log.logging.insert_one(error_log_entry.dict(by_alias=True))
            raise HTTPException(status_code=404, detail=f"Blog by ID:{_id} does not exist")
        else:
            return Blog(**cursor)

    except Exception as e:
        # Log the exception with detailed information
        error_log_entry = Logging(
            route_action=route_path,
            method=route_method,
            client_host=client_host,
            content=f'An error occurred: {str(e)} - PRIVATE',
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            datum_vnosa=datetime.datetime.now()
        )
        proces_log.logging.insert_one(error_log_entry.dict(by_alias=True))

        # Raise an HTTPException with a 500 Internal Server Error status code
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail='Internal Server Error'
        )


# Add blog for Admin
@router.post("/admin", operation_id="add_blog_admin")
async def post_one_admin(request: Request, blog: Blog, current_user: str = Depends(get_current_user)) -> Blog | None:
    """
    This route adds a new blog to the database.

    Parameters:
    - blog (Blog): The blog object to be added.
    - current_user (str): The username of the authenticated user.

    Behavior:
    - Adds a new blog to the database.
    - Returns the added Blog object if successful, or None if unsuccessful.
    """

    # Get the path of the current route from the request
    route_path = request.url.path
    route_method = request.method
    client_host = request.client.host

    try:
        # Save route path to logging collection
        log_entry = Logging(
            route_action=route_path,
            method=route_method,
            client_host=client_host,
            content='Request made to: ADD BLOG - PRIVATE',
            status_code=status.HTTP_200_OK,
            datum_vnosa=datetime.datetime.now()
        )
        proces_log.logging.insert_one(log_entry.dict(by_alias=True))

        # Add a new blog to the database
        blog_dict = blog.dict(by_alias=True)
        insert_result = db.proces.blog.insert_one(blog_dict)

        # Check if the insertion was acknowledged and update the blog's ID
        if insert_result.acknowledged:
            blog_dict['_id'] = str(insert_result.inserted_id)
            return Blog(**blog_dict)
        else:
            return None

    except Exception as e:
        # Log the exception
        error_log_entry = Logging(
            route_action=route_path,
            method=route_method,
            client_host=client_host,
            content=f'An error occurred: {str(e)}',
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            datum_vnosa=datetime.datetime.now()
        )
        proces_log.logging.insert_one(error_log_entry.dict(by_alias=True))

        # Raise an HTTPException with a 500 Internal Server Error status code
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail='Internal Server Error'
        )


# Edit by ID
@router.put("/admin/{_id}", operation_id="edit_blog_admin")
async def edit_blog_admin(request: Request, _id: str, blog: Blog, current_user: str = Depends(get_current_user)) -> Blog | None:
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

    # Get the path of the current route from the request
    route_path = request.url.path
    route_method = request.method
    client_host = request.client.host

    try:
        # Save route path to logging collection
        log_entry = Logging(
            route_action=route_path,
            method=route_method,
            client_host=client_host,
            content=f'Request made to: EDIT BLOG BY ID: {_id} - PRIVATE',
            status_code=status.HTTP_200_OK,
            datum_vnosa=datetime.datetime.now()
        )
        proces_log.logging.insert_one(log_entry.dict(by_alias=True))

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

        # Log unsuccessful update
        error_log_entry = Logging(
            route_action=route_path,
            method=route_method,
            client_host=client_host,
            content=f'Blog with ID {_id} not updated',
            status_code=status.HTTP_400_BAD_REQUEST,
            datum_vnosa=datetime.datetime.now()
        )
        proces_log.logging.insert_one(error_log_entry.dict(by_alias=True))

        # Return None if the blog was not updated
        return None

    except Exception as e:
        # Log the exception
        error_log_entry = Logging(
            route_action=route_path,
            method=route_method,
            client_host=client_host,
            content=f'An error occurred: {str(e)}',
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            datum_vnosa=datetime.datetime.now()
        )
        proces_log.logging.insert_one(error_log_entry.dict(by_alias=True))

        # Raise an HTTPException with a 500 Internal Server Error status code
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail='Internal Server Error'
        )


# Delete a blog by its ID from the database
@router.delete("/admin/{_id}", operation_id="delete_blog_admin")
async def delete_blog_admin(request: Request, _id: str):
    """
    Route to delete a blog by its ID from the database.

    Arguments:
        _id (str): The ID of the blog to be deleted.
        current_user (str): The current authenticated user.

    Returns:
        dict: A message indicating the status of the deletion.

    Raises:
        HTTPException: If the blog is not found for deletion.
        :param current_user: authentication
        :param _id: ID of the blog
        :param request: path to the request
    """

    # Get the path of the current route from the request
    route_path = request.url.path
    route_method = request.method
    client_host = request.client.host

    # Save route path to logging collection
    log_entry = Logging(
        route_action=route_path,
        method=route_method,
        client_host=client_host,
        content=f'Request made to: DELETE BLOG BY ID: {_id} - PRIVATE',
        status_code=status.HTTP_200_OK,
        datum_vnosa=datetime.datetime.now()
    )
    proces_log.logging.insert_one(log_entry.dict(by_alias=True))

    # Attempt to delete the blog from the database
    delete_result = db.proces.blog.delete_one({'_id': _id})

    # Check if the blog was successfully deleted
    if delete_result.deleted_count > 0:
        return {"message": "Blog deleted successfully"}
    else:

        # Log the error and raise HTTPException for 404
        error_log_entry = Logging(
            route_action=route_path,
            method=route_method,
            client_host=client_host,
            content=f'Blog with ID {_id} not found - PRIVATE',
            status_code=status.HTTP_404_NOT_FOUND,
            datum_vnosa=datetime.datetime.now()
        )
        proces_log.logging.insert_one(error_log_entry.dict(by_alias=True))

        # Raise an exception if the blog was not found for deletion
        raise HTTPException(status_code=404, detail=f"Blog by ID:({_id}) not found")
