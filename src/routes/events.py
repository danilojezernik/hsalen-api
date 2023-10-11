"""
This module defines API routes for managing events.

Routes:
1. GET all events
2. GET event by ID
3. ADD a new event
4. Edit an existing event by ID
5. Delete an event by ID
"""

# Import necessary modules and classes
from fastapi import APIRouter, HTTPException, Depends
from src.services import db
from src.domain.events import Events
from src.services.security import get_current_user

# Create a router for handling event related endpoints
router = APIRouter()


# GET ALL EVENT
@router.get('/', operation_id="get_all_event")
def get_event() -> list[Events]:
    """
    Route to get all event from the database.

    Returns:
        list[event]: List of all event in the database.
    """

    # Retrieve all event from the database
    cursor = db.proces.event.find()
    return [Events(**document) for document in cursor]


# ADMIN

# GET ALL EVENT FOR ADMIN
@router.get('/admin/', operation_id="get_all_event_admin")
def get_event_admin(current_user: str = Depends(get_current_user)) -> list[Events]:
    """
    Route to get all event from the database for admin.

    Returns:
        list[event]: List of all event in the database.
    """

    # Retrieve all event from the database
    cursor = db.proces.event.find()
    return [Events(**document) for document in cursor]


# GET EVENT BY ID
@router.get("/admin/{_id}", operation_id="get_event_by_id_admin")
async def get_event_id_admin(_id: str, current_user: str = Depends(get_current_user)):
    """
    Route to get an event by its ID from the database for admin.

    Arguments:
        _id (str): The ID of an event to retrieve.

    Returns:
        event: The event with the specified ID.

    Raises:
        HTTPException: If event with the specified ID is not found.
    """

    # Retrieve an event by its ID from the database
    cursor = db.proces.event.find_one({'_id': _id})
    if cursor is None:
        raise HTTPException(status_code=404, detail=f"Event by ID:{_id} does not exist")
    else:
        return Events(**cursor)


# ADD EVENT FOR ADMIN
@router.post("/admin", operation_id="add_event_admin")
async def post_one_admin(event: Events, current_user: str = Depends(get_current_user)) -> Events | None:
    """
    Route to add a new event to the database for admin.

    Arguments:
        event (event): The event object to be added.

    Returns:
        event: The added event.

    Notes:
        If the insertion fails, None is returned.
    """

    # Convert event object to a dictionary
    event_dict = event.dict(by_alias=True)

    # Insert the event dictionary into the database
    insert_result = db.proces.event.insert_one(event_dict)

    # Update the event dictionary with the inserted ID
    if insert_result.acknowledged:
        event_dict['_id'] = str(insert_result.inserted_id)

        # Return the event object created from the inserted dictionary
        return Events(**event_dict)

    # Return None if insertion failed
    return None


# EDIT EVENT FOR ADMIN
@router.put("/admin/{_id}", operation_id="edit_event_admin")
async def edit_event_admin(_id: str, event: Events, current_user: str = Depends(get_current_user)) -> Events | None:
    """
    Route to edit an existing event by its ID in the database for admin.

    Arguments:
        _id (str): The ID of the event to edit.
        event (event): The updated event object.

    Returns:
        event: The updated event.

    Raises:
        HTTPException: If the event is not found for editing.
    """

    # Convert the event object to a dictionary and remove the ID field
    event = event.dict(by_alias=True)
    del event['_id']

    # Update the event document in the database based on its ID
    cursor = db.proces.event.update_one({'_id': _id}, {'$set': event})

    # Check if the update was successful based on modified count
    if cursor.modified_count > 0:
        # Retrieve the updated document from the database
        updated_document = db.proces.event.find_one({'_id': _id})

        # Return the updated event object
        if updated_document:
            updated_document['_id'] = str(updated_document['_id'])
            return Events(**updated_document)

    # Return None if the update failed
    return None


# DELETE EVENT FOR ADMIN
@router.delete("/admin/{_id}", operation_id="delete_event_admin")
async def delete_event_admin(_id: str, current_user: str = Depends(get_current_user)):
    """
    Route to delete an event by its ID from the database for admin.

    Arguments:
        _id (str): The ID of the event to delete.

    Returns:
        dict: A message indicating the status of the deletion.

    Raises:
        HTTPException: If the event is not found for deletion.
    """

    # Delete an event by its ID from the database
    delete_result = db.proces.event.delete_one({'_id': _id})

    # Check if delete was successful based on deleted count
    if delete_result.deleted_count > 0:
        # Return a success message if event was deleted
        return {"message": f"Event with id:({_id}) deleted successfully"}
    else:
        # Raise an HTTPException if event was not found
        raise HTTPException(status_code=404, detail=f"Event by ID:({_id}) not found")
