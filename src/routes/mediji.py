"""
This module defines API routes for managing medije.

Routes:
1. GET all mediji
2. GET mediji by ID
3. ADD a new mediji
4. Edit an existing mediji by ID
5. Delete a mediji by ID
"""

# Import necessary modules and classes
from fastapi import APIRouter, HTTPException, Depends
from src.services import db
from src.domain.mediji import Mediji
from src.domain.logging import Logging

from src.services.security import get_current_user

# Create a router for handling Mediji related endpoints
router = APIRouter()


# GET ALL MEDIJI
@router.get('/', operation_id="get_all_mediji")
def get_mediji() -> list[Mediji]:
    """
    Route to get all Mediji from the database.

    Returns:
        list[Mediji]: List of all Mediji in the database.
    """

    # Retrieve all mediji from the database
    cursor = db.proces.mediji.find()
    return [Mediji(**document) for document in cursor]


# ADMIN

# GET ALL MEDIJI FOR ADMIN
@router.get('/admin/', operation_id="get_all_mediji_admin")
def get_mediji_admin(current_user: str = Depends(get_current_user)) -> list[Mediji]:
    """
    Route to get all Mediji from the database for admin.

    Returns:
        list[Mediji]: List of all Mediji in the database.
    """

    logging_dict = Logging(route_action='Get all Medija admin').dict(by_alias=True)

    db.proces.logging.insert_one(logging_dict)

    # Retrieve all mediji from the database
    cursor = db.proces.mediji.find()
    return [Mediji(**document) for document in cursor]


# GET MEDIJI BY ID
@router.get("/admin/{_id}", operation_id="get_mediji_by_id_admin")
async def get_mediji_id_admin(_id: str, current_user: str = Depends(get_current_user)):
    """
    Route to get a Mediji by its ID from the database for admin.

    Arguments:
        _id (str): The ID of the Mediji to retrieve.

    Returns:
        Mediji: The Mediji with the specified ID.

    Raises:
        HTTPException: If the Mediji with the specified ID is not found.
    """

    # Retrieve a mediji by its ID from the database
    cursor = db.proces.mediji.find_one({'_id': _id})
    if cursor is None:
        raise HTTPException(status_code=404, detail=f"Mediji by ID:{_id} does not exist")
    else:
        return Mediji(**cursor)


# ADD MEDIJI FOR ADMIN
@router.post("/admin", operation_id="add_mediji_admin")
async def post_one_admin(mediji: Mediji, current_user: str = Depends(get_current_user)) -> Mediji | None:
    """
    Route to add a new Mediji to the database for admin.

    Arguments:
        mediji (Mediji): The Mediji object to be added.

    Returns:
        Mediji: The added Mediji.

    Notes:
        If the insertion fails, None is returned.
    """

    # Convert Mediji object to a dictionary
    mediji_dict = mediji.dict(by_alias=True)

    # Insert the Mediji dictionary into the database
    insert_result = db.proces.mediji.insert_one(mediji_dict)

    # Update the Mediji dictionary with the inserted ID
    if insert_result.acknowledged:
        mediji_dict['_id'] = str(insert_result.inserted_id)

        # Return the Mediji object created from the inserted dictionary
        return Mediji(**mediji_dict)

    # Return None if insertion failed
    return None


# EDIT MEDIJI FOR ADMIN
@router.put("/admin/{_id}", operation_id="edit_mediji_admin")
async def edit_mediji_admin(_id: str, mediji: Mediji, current_user: str = Depends(get_current_user)) -> Mediji | None:
    """
    Route to edit an existing Mediji by its ID in the database for admin.

    Arguments:
        _id (str): The ID of the Mediji to edit.
        mediji (Mediji): The updated Mediji object.

    Returns:
        Mediji: The updated Mediji.

    Raises:
        HTTPException: If the Mediji is not found for editing.
    """

    # Convert the Mediji object to a dictionary and remove the ID field
    mediji = mediji.dict(by_alias=True)
    del mediji['_id']

    # Update the Mediji document in the database based on its ID
    cursor = db.proces.mediji.update_one({'_id': _id}, {'$set': mediji})

    # Check if the update was successful based on modified count
    if cursor.modified_count > 0:
        # Retrieve the updated document from the database
        updated_document = db.proces.mediji.find_one({'_id': _id})

        # Return the updated Mediji object
        if updated_document:
            updated_document['_id'] = str(updated_document['_id'])
            return Mediji(**updated_document)

    # Return None if the update failed
    return None


# DELETE MEDIJI FOR ADMIN
@router.delete("/admin/{_id}", operation_id="delete_mediji_admin")
async def delete_mediji_admin(_id: str, current_user: str = Depends(get_current_user)):
    """
    Route to delete a Mediji by its ID from the database for admin.

    Arguments:
        _id (str): The ID of the Mediji to delete.

    Returns:
        dict: A message indicating the status of the deletion.

    Raises:
        HTTPException: If the Mediji is not found for deletion.
    """

    # Delete a Mediji by its ID from the database
    delete_result = db.proces.mediji.delete_one({'_id': _id})

    # Check if delete was successful based on deleted count
    if delete_result.deleted_count > 0:
        # Return a success message if Mediji was deleted
        return {"message": f"Mediji with id:({_id}) deleted successfully"}
    else:
        # Raise an HTTPException if Mediji was not found
        raise HTTPException(status_code=404, detail=f"Mediji by ID:({_id}) not found")
