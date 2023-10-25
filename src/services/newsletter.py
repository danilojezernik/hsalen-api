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
        bool: True if the newsletter email was sent successfully, False otherwise.

    Note:
        This function sends a newsletter email to a list of subscribers. It uses the SMTP protocol to send the email.
        Before using this function, make sure to set up the Gmail sender email and password in the environment variables
        'env.EMAIL_ME' and 'env.EMAIL_PASSWORD'. Additionally, the 'env.EMAIL_ME' should be set to the same Gmail account
        used for SMTP login.

    Dependencies:
        - Python's smtplib module for sending emails
    """
    # Retrieve email addresses of subscribers from the database
    cursor = db.proces.newsletter.find({}, {'email': 1})
    email_addresses = [document['email'] for document in cursor]

    # Create an EmailMessage object
    em = EmailMessage()
    em['From'] = env.EMAIL_ME
    em['Subject'] = subject
    em.set_content(body, subtype='html')

    # Set CC recipients as a comma-separated string of email addresses
    cc_recipients = ", ".join(email_addresses)
    em['CC'] = cc_recipients

    # TODO: ALENU NASTAVI GOOGLE PASSWORD ZA DOBIVANJE EMAILOV - PASSWORD + SENDER
    # Establish an SSL connection to Gmail's SMTP server
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(env.EMAIL_ME, env.EMAIL_PASSWORD)

        # Send the email to env.EMAIL_ME (sender) with CC to all email addresses
        sendemail = smtp.sendmail(env.EMAIL_ME, [env.EMAIL_ME] + email_addresses, em.as_string())

        if not sendemail:
            return True  # Newsletter email sent successfully
        else:
            return False  # Failed to send the newsletter email
