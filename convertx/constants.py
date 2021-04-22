from dotenv import load_dotenv
import os


DOTENV_PATH = r'C:\Users\natha\PycharmProjects\convertx\env\.env'  # this is a constant
load_dotenv(dotenv_path=DOTENV_PATH)

DOMAIN_NAME = 'convertxproject.com'
DOMAIN_NAME_WWW = 'www.convertxproject.com'
DOMAIN_NAME_HTTPS = 'https://convertxproject.com'
DOMAIN_HEROKU = 'convertxproject.herokuapp.com'

SUPERUSER_USERNAME = os.getenv('SUPERUSER_USERNAME')
SUPERUSER_EMAIL = os.getenv('SUPERUSER_EMAIL')
SUPERUSER_PASSWORD = os.getenv('SUPERUSER_PASSWORD')
