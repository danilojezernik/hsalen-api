"""
This module defines API routes for managing blogs.

Routes:
1. GET index to insert log
"""

# Import necessary modules and classes
import datetime

from fastapi import APIRouter, HTTPException, Request, status

import urllib.request
import json

from src.domain.logs import Logging
from src.services import db

router = APIRouter()


# GET ALL BLOG
@router.get("/", operation_id="get_index")
async def get_all(request: Request):
    """
    This route handles the retrieval of all blogs from the database.

    Behavior:
    - Insert logs to admin action
    - Returns a list of Blog objects.
    """
    route_path = request.url.path
    route_method = request.method
    client_host = request.client.host

    with urllib.request.urlopen("https://geolocation-db.com/json") as url:
        data = json.loads(url.read().decode())

    city = data.get("city", "City Not Found")

    try:
        log_entry = Logging(
            route_action=route_path,
            domain='BACKEND',
            client_host=client_host,
            city=city,
            content=f'Request made to: INDEX - {route_method} ',
            datum_vnosa=datetime.datetime.now()
        )
        db.log.backend_logs.insert_one(log_entry.dict(by_alias=True))

        # Include the city in the response JSON
        return {'message': 'Index initialized'}

    except Exception as e:
        error_log_entry = Logging(
            route_action=route_path,
            domain='BACKEND',
            client_host=client_host,
            city=city,
            content=f'An error occurred: {str(e)}',
            datum_vnosa=datetime.datetime.now()
        )

        db.log.backend_logs.insert_one(error_log_entry.dict(by_alias=True))

        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail='Internal Server Error'
        )