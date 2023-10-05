import os

from dotenv import load_dotenv

load_dotenv()
PORT = os.getenv('PORT')
DB_CONNECTION = os.getenv('DB_CONNECTION')
DB_PROCES = os.getenv('DB_PROCES')
SECRET_KEY = os.getenv('SECRET_KEY')
UPORABNIK = os.getenv('UPORABNIK')
GESLO = os.getenv('GESLO')
ALGORITHM = os.getenv('ALGORITHM')
EMAIL_PASSWORD = os.getenv('EMAIL_PASSWORD')
EMAIL_ME = os.getenv('EMAIL_ME')