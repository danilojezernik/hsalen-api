from fastapi import APIRouter, HTTPException

from src.services import emails, db

router = APIRouter()


# TODO: remove later when functionality is implemented for other routes
# GET ONLY EMAILS FROM THE DATABASE
@router.get("/")
async def get_emails_only() -> list[str]:
    """
    Route for retrieving a list of email addresses from the database.

    Returns:
        list[str]: A list of email addresses.

    Note:
        This route does not send emails but is used to fetch email addresses from the database.
    """

    # Retrieve email addresses from the database
    cursor = db.proces.newsletter.find({}, {'email': 1})

    # Extract just the 'email' field from the cursor
    email_addresses = [document['email'] for document in cursor]

    return email_addresses  # Return a list of email addresses


# SEND NEWSLETTER TO ALL
@router.post("/send-newsletter")
async def send_emails_to_all():

    # Send the emails to all
    if not emails.newsletter(subject='Hypnosis Studio Alen | E-novice ♥', body='TESTING'):
        return HTTPException(status_code=500, detail="Email not sent")

    return {"message": "Newsletter was sent"}

