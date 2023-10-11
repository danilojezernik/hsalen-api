from fastapi import APIRouter, HTTPException, Depends

from src.domain.mail import Email
from src.services import emails, db
from src.template import email
from src.services.security import get_current_user

router = APIRouter()


# USER SENDING EMAIL TO AUTHOR
@router.post("/send-email")
async def user_send_email(emailing: Email):
    body = email.html(name=emailing.name, surname=emailing.surname, email=emailing.email, content=emailing.content)

    if not emails.send(email_from=emailing.email, subject='Hypnosis Studio Alen | Dobil si sporočilo ♥', body=body):
        return HTTPException(status_code=500, detail="Email not sent")

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
    cursor = db.proces.email.find()
    return [Email(**document) for document in cursor]


# ADMIN DELETE EMAIL
@router.delete("/{_id}", operation_id="delete_email_admin")
async def delete_email_admin(_id: str, current_user: str = Depends(get_current_user)):
    """
    Route to delete an email by its ID from the database.

    Arguments:
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
