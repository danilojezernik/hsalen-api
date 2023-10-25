from email.message import EmailMessage
import smtplib

from src import env
from src.services import db


def newsletter(subject: str, body: str) -> bool:
    cursor = db.proces.newsletter.find({}, {'email': 1})
    email_addresses = [document['email'] for document in cursor]

    em = EmailMessage()
    em['From'] = env.EMAIL_ME
    em['Subject'] = subject
    em.set_content(body, subtype='html')

    # Set CC recipients as a comma-separated string of email addresses
    cc_recipients = ", ".join(email_addresses)
    em['CC'] = cc_recipients

    # TODO: ALENU NASTAVI GOOGLE PASSWORD ZA DOBIVANJE EMAILOV - PASSWORD + SENDER
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(env.EMAIL_ME, env.EMAIL_PASSWORD)

        # Send the email to env.EMAIL_ME (sender) with CC to all email addresses
        sendemail = smtp.sendmail(env.EMAIL_ME, [env.EMAIL_ME] + email_addresses, em.as_string())

        if not sendemail:
            return True
        else:
            return False
