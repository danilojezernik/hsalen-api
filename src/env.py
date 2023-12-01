import os

from dotenv import load_dotenv

load_dotenv()
PORT = int(os.getenv('PORT'))
DB_CONNECTION = str(os.getenv('DB_CONNECTION'))
DB_PROCES = str(os.getenv('DB_PROCES'))
SECRET_KEY = str(os.getenv('SECRET_KEY'))
UPORABNIK = str(os.getenv('UPORABNIK'))
GESLO = str(os.getenv('GESLO'))
ALGORITHM = str(os.getenv('ALGORITHM'))
EMAIL_PASSWORD = str(os.getenv('EMAIL_PASSWORD'))
EMAIL_ME = str(os.getenv('EMAIL_ME'))
DOMAIN = str(os.getenv('DOMAIN'))
DB_PROCES_LOGGING = str(os.getenv('DB_PROCES_LOGGING'))
DB_CONNECTION_LOGGING = str(os.getenv('DB_CONNECTION_LOGGING'))

# TESTING
EMAIL_1 = str(os.getenv('EMAIL_1'))
EMAIL_2 = str(os.getenv('EMAIL_2'))