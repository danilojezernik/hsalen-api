import ssl
from email.message import EmailMessage
import smtplib

from src import env


def send(email_from: str, subject: str, body: str) -> bool:
    """
    Send an email to a specified recipient.

    Args:
        email_from (str): The recipient's email address.
        subject (str): The subject of the email.
        body (str): The HTML content of the email.

    Returns:
        bool: True if the email was sent successfully, False otherwise.

    Note:
        This function sends an email to a specified recipient using the SMTP protocol to connect to Gmail's SMTP server.
        It's intended for sending individual emails. Before using this function, ensure that you have set up the Gmail
        sender email and password in the environment variables 'env.EMAIL_ME' and 'env.EMAIL_PASSWORD'. Additionally,
        the 'env.EMAIL_ME' should be set to the same Gmail account used for SMTP login.

    Dependencies:
        - Python's smtplib module for sending emails
    """
    # Create an EmailMessage object
    em = EmailMessage()
    em['From'] = email_from
    em['To'] = env.EMAIL_ME
    em['Subject'] = subject
    em.set_content(body, subtype='html')

    context = ssl.create_default_context()

    # TODO: ALENU NASTAVI GOOGLE PASSWORD ZA DOBIVANJE EMAILOV - PASSWORD + SENDER
    # Establish an SSL connection to Gmail's SMTP server
    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
        smtp.login(env.EMAIL_ME, env.EMAIL_PASSWORD)

        # Send the email from 'env.EMAIL_ME' to 'email_from'
        sendemail = smtp.sendmail(env.EMAIL_ME, env.EMAIL_ME, em.as_string())

        if not sendemail:
            return True  # Email sent successfully
        else:
            return False  # Failed to send the email
