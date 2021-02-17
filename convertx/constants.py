from dotenv import load_dotenv
import os


DOTENV_PATH = r'C:\Users\natha\PycharmProjects\convertx\env\.env'  # this is a constant
load_dotenv(dotenv_path=DOTENV_PATH)


SUPERUSER_USERNAME = os.getenv('SUPERUSER_USERNAME')
