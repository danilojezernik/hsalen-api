from email.message import EmailMessage
import smtplib

from src import env


def send_email(email_from: str, subject: str, body: str) -> bool:
    em = EmailMessage()
    em['From'] = env.EMAIL_ME
    em['To'] = email_from
    em['Subject'] = subject
    em.set_content(body, subtype='html')

    # TODO: ALENU NASTAVI GOOGLE PASSWORD ZA DOBIVANJE EMAILOV - PASSWORD + SENDER
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:

        smtp.login(env.EMAIL_ME, env.EMAIL_PASSWORD)
        sendemail = smtp.sendmail(env.EMAIL_ME, env.EMAIL_ME, em.as_string())
        if not sendemail:
            return True
        else:
            return False
