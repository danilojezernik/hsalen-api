"""
This module defines API routes for managing reviews.

Routes:
1. GET all reviews
2. GET review by ID
3. ADD a new review
4. Edit an existing review by ID
5. Delete a review by ID
"""

# Import necessary modules and classes
from fastapi import APIRouter, HTTPException, Depends
from src.services import db
from src.domain.review import Review
from src.services.security import get_current_user

# Create a router for handling event related endpoints
router = APIRouter()


# GET ALL REVIEWS
@router.get('/', operation_id="get_all_reviews")
def get_reviews() -> list[Review]:
    """
    Route to get all reviews from the database.

    Returns:
        list[event]: List of all reviews in the database.
    """

    # Retrieve all reviews from the database
    cursor = db.proces.review.find()
    return [Review(**document) for document in cursor]


# GET REVIEW BY ID
@router.get("/{_id}", operation_id="get_review_by_id")
async def get_review_by_id(_id: str, current_user: str = Depends(get_current_user)):
    """
    Route to get a review by its ID from the database.

    Arguments:
        _id (str): The ID of a review to retrieve.

    Returns:
        event: The review with the specified ID.

    Raises:
        HTTPException: If review with the specified ID is not found.
    """

    # Retrieve an event by its ID from the database
    cursor = db.proces.event.find_one({'_id': _id})
    if cursor is None:
        raise HTTPException(status_code=404, detail=f"Review by ID:{_id} does not exist")
    else:
        return Review(**cursor)


# ADD REVIEW
@router.post("/", operation_id="add_review")
async def post_one(review: Review, current_user: str = Depends(get_current_user)) -> Review | None:
    """
    Route to add a new review to the database.

    Arguments:
        review (review): The review object to be added.

    Returns:
        review: The added review.

    Notes:
        If the insertion fails, None is returned.
    """

    # Convert review object to a dictionary
    review_dict = review.dict(by_alias=True)

    # Insert the review dictionary into the database
    insert_result = db.proces.review.insert_one(review_dict)

    # Update the review dictionary with the inserted ID
    if insert_result.acknowledged:
        review_dict['_id'] = str(insert_result.inserted_id)

        # Return the review object created from the inserted dictionary
        return Review(**review_dict)

    # Return None if insertion failed
    return None


# EDIT REVIEW
@router.put("/{_id}", operation_id="edit_review")
async def edit_review(_id: str, review: Review, current_user: str = Depends(get_current_user)) -> Review | None:
    """
    Route to edit an existing review by its ID in the database.

    Arguments:
        _id (str): The ID of the review to edit.
        review (event): The updated review object.

    Returns:
        event: The updated review.

    Raises:
        HTTPException: If the review is not found for editing.
    """

    # Convert the review object to a dictionary and remove the ID field
    review = review.dict(by_alias=True)
    del review['_id']

    # Update the review document in the database based on its ID
    cursor = db.proces.review.update_one({'_id': _id}, {'$set': review})

    # Check if the update was successful based on modified count
    if cursor.modified_count > 0:
        # Retrieve the updated document from the database
        updated_document = db.proces.review.find_one({'_id': _id})

        # Return the updated review object
        if updated_document:
            updated_document['_id'] = str(updated_document['_id'])
            return Review(**updated_document)

    # Return None if the update failed
    return None


# DELETE REVIEW
@router.delete("/{_id}", operation_id="delete_review")
async def delete_review(_id: str, current_user: str = Depends(get_current_user)):
    """
    Route to delete a review by its ID from the database.

    Arguments:
        _id (str): The ID of the review to delete.

    Returns:
        dict: A message indicating the status of the deletion.

    Raises:
        HTTPException: If the review is not found for deletion.
    """

    # Delete a review by its ID from the database
    delete_result = db.proces.review.delete_one({'_id': _id})

    # Check if delete was successful based on deleted count
    if delete_result.deleted_count > 0:
        # Return a success message if event was deleted
        return {"message": f"Review with id:({_id}) deleted successfully"}
    else:
        # Raise an HTTPException if event was not found
        raise HTTPException(status_code=404, detail=f"Review by ID:({_id}) not found")
