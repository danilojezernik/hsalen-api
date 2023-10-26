from fastapi import APIRouter, HTTPException, Depends

from src.domain.subscriber import Subscriber
from src.services import newsletter, db
from src.services.security import get_current_user

router = APIRouter()


# GET ALL SUBSCRIBERS
@router.get("/", operation_id="get_all_subscribers")
async def get_all_subscribers(current_user: str = Depends(get_current_user)) -> list[Subscriber]:
    """
    This route handles the retrieval of all subscribers from the database.

    Behavior:
    - Retrieves all subscribers from the database.
    - Returns a list of Subscriber objects.
    """

    cursor = db.proces.subscriber.find()
    return [Subscriber(**document) for document in cursor]


# ADD SUBSCRIBER
@router.post("/", operation_id="add_SUBSCRIBER")
async def post_one_admin(subscriber: Subscriber, current_user: str = Depends(get_current_user)) -> Subscriber | None:
    """
    This route adds a new subscriber to the database.

    Parameters:
    - subscriber (Subscriber): The subscriber object to be added.
    - current_user (str): The username of the authenticated user.

    Behavior:
    - Adds a new subscriber to the database.
    - Returns the added Subscriber object if successful, or None if unsuccessful.
    """

    # Add a new blog to the database
    subscriber_dict = subscriber.dict(by_alias=True)
    insert_result = db.proces.subscriber.insert_one(subscriber_dict)

    # Check if the insertion was acknowledged and update the blog's ID
    if insert_result.acknowledged:
        subscriber_dict['_id'] = str(insert_result.inserted_id)
        return Subscriber(**subscriber_dict)
    else:
        return None


# EDIT SUBSCRIBER BY ID
@router.put("/{_id}")
async def edit_subscriber(_id: str, subscriber: Subscriber, current_user: str = Depends(get_current_user)) -> Subscriber | None:
    """
    This route edits an existing subscriber by its ID in the database.

    Parameters:
    - _id (str): The ID of the subscriber to be edited.
    - blog (Blog): The updated subscriber object.
    - current_user (str): The username of the authenticated user.

    Behavior:
    - Edits an existing subscriber by its ID in the database.
    - Returns the updated Subscriber object if successful, or None if unsuccessful.
    """

    # Edit an existing subscriber by its ID in the database
    subscriber = subscriber.dict(by_alias=True)
    del subscriber['_id']

    # Update the newsletter in the database
    cursor = db.proces.subscriber.update_one({'_id': _id}, {'$set': subscriber})

    # Check if the newsletter was successfully updated
    if cursor.modified_count > 0:
        # Retrieve the updated newsletter from the database
        updated_document = db.proces.subscriber.find_one({'_id': _id})

        # Check if the updated newsletter exists
        if updated_document:
            updated_document['_id'] = str(updated_document['_id'])
            return Subscriber(**updated_document)

    # Return None if the newsletter was not updated
    return None


# Delete a blog by its ID from the database
@router.delete("/{_id}", operation_id="delete_subscriber")
async def delete_subscriber(_id: str, current_user: str = Depends(get_current_user)):
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
    delete_result = db.proces.subscriber.delete_one({'_id': _id})

    # Check if the blog was successfully deleted
    if delete_result.deleted_count > 0:
        return {"message": "Subscriber deleted successfully"}
    else:
        # Raise an exception if the blog was not found for deletion
        raise HTTPException(status_code=404, detail=f"Subscriber by ID:({_id}) not found")


# TODO: remove later when functionality is implemented for other routes
# GET ONLY EMAILS FROM THE DATABASE
@router.get("/", operation_id="get_emails_of_subscribers")
async def get_emails_only(current_user: str = Depends(get_current_user)) -> list[str]:
    """
    Route for retrieving a list of email addresses from the database.

    Returns:
        list[str]: A list of email addresses.

    Note:
        This route does not send emails but is used to fetch email addresses from the database.
    """

    # Retrieve email addresses from the database
    cursor = db.proces.subscriber.find({}, {'email': 1})

    # Extract just the 'email' field from the cursor
    email_addresses = [document['email'] for document in cursor]

    return email_addresses  # Return a list of email addresses


# SEND NEWSLETTER TO ALL
@router.post("/send-newsletter", operation_id="send_newsletter_to_all")
async def send_newsletter_to_all(current_user: str = Depends(get_current_user)):
    # Send the newsletter to all
    if not newsletter.newsletter(subject='Hypnosis Studio Alen | E-novice ♥', body='TESTIRAM - SI DOBIL?'):
        return HTTPException(status_code=500, detail="Email not sent")

    return {"message": "Newsletter was sent"}
