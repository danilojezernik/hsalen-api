"""
This module defines API routes for managing blogs.

Routes:
1. GET hypnotherapy to insert log
"""

# Import necessary modules and classes
import datetime

from fastapi import APIRouter, HTTPException, Request, status

from src.domain.logs import Logging
from src.services import db

router = APIRouter()


# GET ALL BLOG
@router.get("/", operation_id="get_hypnotherapy")
async def get_all(request: Request):
    """
    This route stores host to database for analytics.

    Behavior:
    - Insert logs to admin action
    - Returns message or exception.
    """

    # Get the path of the current route from the request
    route_path = request.url.path
    route_method = request.method
    client_host = request.client.host

    try:
        # Save route path to logging collection
        log_entry = Logging(
            route_action=route_path,
            domain='BACKEND',
            client_host=client_host,
            content=f'Request made to: HIPNOTERAPIJA - {route_method} ',
            datum_vnosa=datetime.datetime.now()
        )
        db.log.backend_logs.insert_one(log_entry.dict(by_alias=True))

        return {'message': 'Hipnoterapija initialized'}

    except Exception as e:
        # Log the exception
        error_log_entry = Logging(
            route_action=route_path,
            domain='BACKEND',
            client_host=client_host,
            content=f'An error occurred: {str(e)}',
            datum_vnosa=datetime.datetime.now()
        )

        # Insert the error log entry into the database
        db.log.backend_logs.insert_one(error_log_entry.dict(by_alias=True))

        # Raise an HTTPException with a 500 Internal Server Error status code
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail='Internal Server Error'
        )
