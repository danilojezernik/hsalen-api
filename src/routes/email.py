import datetime

from fastapi import APIRouter, HTTPException, Depends, Request, status

from src.domain.logs import Logging
from src.domain.mail import Email
from src.services import emails, db
from src.template import email
from src.services.security import get_current_user

router = APIRouter()


# CONTACT HYPNOSIS STUDIO ALEN
@router.post("/send-email", operation_id='contact')
async def user_send_email(emailing: Email, request: Request):
    """
    Route for sending an email and storing it in the database.

    Args:
        emailing (Email): The email content provided in the request body.

    Returns:
        dict: A message indicating the status of the email sending and storage.

    Raises:
        HTTPException: If email sending fails or if there's an issue with storing the email data.
        :param request: host
        :param emailing: emails
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
            content=f'Request made to: SEND EMAIL - {route_method}',
            datum_vnosa=datetime.datetime.now()
        )
        db.log.backend_logs.insert_one(log_entry.dict(by_alias=True))

        # Create the email body using HTML content
        body = email.html(name=emailing.name, surname=emailing.surname, email=emailing.email, content=emailing.content)

        # Send the email
        if not emails.send(email_from=emailing.email,
                           subject=f'Hypnosis Studio Alen | {emailing.name} ti je poslal/a sporočilo ♥', body=body):
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


# ADMIN GETTING EMAILS
@router.get("/", operation_id="get_all_emails_admin")
def get_all_emails(current_user: str = Depends(get_current_user)) -> list[Email]:
    """
    Route for retrieving all stored emails from the database.

    Args:
        current_user (str): The currently authenticated user.

    Returns:
        list[Email]: A list of email objects retrieved from the database.
        :param current_user: authenticated
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
