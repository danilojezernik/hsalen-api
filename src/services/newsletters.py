from email.message import EmailMessage
import smtplib
from src import env
from src.services import db


def newsletter(subject: str, body: str) -> bool:
    """
    Send a newsletter email to a list of subscribers.

    Args:
        subject (str): The subject of the newsletter email.
        body (str): The HTML content of the newsletter email.

    Returns:
        bool: True if the newsletter email was sent successfully to all subscribers, False otherwise.
    """
    try:
        # Retrieve email addresses of subscribers from the database
        cursor = db.proces.subscriber.find({}, {'email': 1})
        email_addresses = [document['email'] for document in cursor]

        # Establish an SSL connection to Gmail's SMTP server
        with smtplib.SMTP_SSL('smtp.gmail.com', 587) as smtp:
            smtp.login(env.EMAIL_ME, env.EMAIL_PASSWORD)

            for recipient in email_addresses:
                # Create an EmailMessage object for each recipient
                em = EmailMessage()
                em['From'] = env.EMAIL_ME
                em['To'] = recipient
                em['Subject'] = subject
                em.set_content(body, subtype='html')

                # Send the email to the individual recipient
                smtp.send_message(em)

        return True  # Newsletter email sent successfully to all subscribers

    except smtplib.SMTPException as e:
        print(f"SMTP error occurred: {e}")
        return False
    except Exception as e:
        print(f"General error occurred: {e}")
        return False
