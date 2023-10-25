from fastapi import APIRouter, HTTPException, Depends

from src.domain.mail import Email
from src.services import emails, db
from src.template import email
from src.services.security import get_current_user


router = APIRouter()


# USER SENDING EMAIL TO AUTHOR
@router.post("/send-email")
async def user_send_email(emailing: Email):
    """
    Route for sending an email and storing it in the database.

    Args:
        emailing (Email): The email content provided in the request body.

    Returns:
        dict: A message indicating the status of the email sending and storage.

    Raises:
        HTTPException: If email sending fails or if there's an issue with storing the email data.
    """

    # Create the email body using HTML content
    body = email.html(name=emailing.name, surname=emailing.surname, email=emailing.email, content=emailing.content)

    # Send the email
    if not emails.send(email_from=emailing.email, subject='Hypnosis Studio Alen | Dobil si sporočilo ♥', body=body):
        return HTTPException(status_code=500, detail="Email not sent")

    # Store email data in the database
    email_data = {
        "_id": emailing.id,
        "name": emailing.name,
        "surname": emailing.surname,
        "email": emailing.email,
        "content": emailing.content,
        "datum_vnosa": emailing.datum_vnosa
    }
    db.proces.email.insert_one(email_data)

    return {"message": "Message was sent"}


# ADMIN GETTING EMAILS
@router.get("/", operation_id="get_all_emails_admin")
def get_all_emails(current_user: str = Depends(get_current_user)) -> list[Email]:
    """
    Route for retrieving all stored emails from the database.

    Args:
        current_user (str): The currently authenticated user.

    Returns:
        list[Email]: A list of email objects retrieved from the database.
    """

    # Retrieve all emails from the database
    cursor = db.proces.email.find()
    return [Email(**document) for document in cursor]


# ADMIN DELETE EMAIL
@router.delete("/{_id}", operation_id="delete_email_admin")
async def delete_email_admin(_id: str, current_user: str = Depends(get_current_user)):
    """
    Route to delete an email by its ID from the database.

    Args:
        _id (str): The ID of an email to be deleted.
        current_user (str): The current authenticated user.

    Returns:
        dict: A message indicating the status of the deletion.

    Raises:
        HTTPException: If email is not found for deletion.
    """

    # Attempt to delete email from the database
    delete_result = db.proces.email.delete_one({'_id': _id})

    # Check if email was successfully deleted
    if delete_result.deleted_count > 0:
        return {"message": "Email deleted successfully"}
    else:
        # Raise an exception if email was not found for deletion
        raise HTTPException(status_code=404, detail=f"Email by ID: ({_id}) not found")
