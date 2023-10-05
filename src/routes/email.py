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
def get_all_emails(current_user: str = Depends(get_current_user)):
    cursor = db.proces.email.find()
    return [Email(**document) for document in cursor]


# GET EMAIL BY ID
@router.get("/{_id}", operation_id="get_email_by_id_admin")
async def get_email_by_id_admin(_id: str, current_user: str = Depends(get_current_user)):
    """
    This route handles the retrieval of an email by its ID from the database.

    Parameters:
    - _id (str): ID of the email to retrieve.

    Behavior:
    - Retrieves an email by its ID from the database.
    - Returns the Email object if found, or raises an exception if not found.
    """

    # Retrieve a blog by its ID from the database
    cursor = db.proces.email.find_one({'_id': _id})
    if cursor is None:
        raise HTTPException(status_code=400, detail=f"Email by ID:{_id} does not exist")
    else:
        return Email(**cursor)