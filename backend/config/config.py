import os
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'))


HOST = os.environ.get('HOST')
PORT = os.environ.get('PORT')
DEBUG = os.environ.get('DEBUG')
DATABASE = 'db/db.sqlite'
API_KEY_AI = os.environ.get('API_KEY_AI')

