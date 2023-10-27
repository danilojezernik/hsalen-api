from fastapi import APIRouter, HTTPException

from src.domain.newsletter import Newsletter
from src.services import newsletters, db
from src.template import newsletter_body

router = APIRouter()


# GET ALL NEWSLETTER
@router.get("/", operation_id="get_all_newsletter")
async def get_all_newsletter() -> list[Newsletter]:
    """
    This route handles the retrieval of all newsletter from the database.

    Behavior:
    - Retrieves all newsletter from the database.
    - Returns a list of Newsletter objects.
    """

    cursor = db.proces.newsletter.find()
    return [Newsletter(**document) for document in cursor]


# SEND NEWSLETTER TO ALL
@router.post("/send-newsletter", operation_id="send_newsletter_to_all")
async def send_newsletter_to_all(newsletter: Newsletter):

    # Add a new newsletter to the database
    newsletter_dict = newsletter.dict(by_alias=True)
    insert_result = db.proces.newsletter.insert_one(newsletter_dict)

    body = newsletter_body.html_newsletter(title=newsletter.title, content=newsletter.content)

    # Send the newsletter to all
    if not newsletters.newsletter(subject='Hypnosis Studio Alen | E-novice ♥', body=body):
        return HTTPException(status_code=500, detail="Email not sent")

    # Check if the insertion was acknowledged and update the blog's ID
    if insert_result.acknowledged:
        newsletter_dict['_id'] = str(insert_result.inserted_id)
        return Newsletter(**newsletter_dict)
    else:
        return None
