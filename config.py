from os import environ
from dotenv import load_dotenv


load_dotenv()

API_ID = environ.get('API_ID')
API_HASH = environ.get('API_HASH')
SESSION_STRING = environ.get('SESSION_STRING')
SOURCE_CHANNEL = int(environ.get('SOURCE_CHANNEL'))
TARGET_CHANNEL = int(environ.get('TARGET_CHANNEL'))
