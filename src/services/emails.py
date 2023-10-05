from validate_email import validate_email

from email.message import EmailMessage
import smtplib

from src import env


def exists(email: str) -> bool:
    is_valid = validate_email(email_address=email, check_format=True)
    return is_valid


# TODO: ALENU NASTAVI GOOGLE PASSWORD ZA DOBIVANJE EMAILOV - PASSWORD + SENDER
def send(email_from: str, subject: str, body: str) -> bool:
    em = EmailMessage()
    em['From'] = email_from
    em['To'] = env.EMAIL_ME
    em['Subject'] = subject
    em.set_content(body, subtype='html')

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:

        smtp.login(env.EMAIL_ME, env.EMAIL_PASSWORD)
        sendemail = smtp.sendmail(env.EMAIL_ME, env.EMAIL_ME, em.as_string())
        if not sendemail:
            return True
        else:
            return False
