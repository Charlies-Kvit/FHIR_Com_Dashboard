import random
import string
import os
import json
from time import sleep
from dotenv import load_dotenv
from config.create_token import create_token

create_token(20)
sleep(2)
with open('config/token.json', 'r') as json_file:
    json_data = json.load(json_file)

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'))

HOST = os.environ.get('HOST')
PORT = os.environ.get('PORT')
DEBUG = bool(int(os.environ.get('DEBUG')))
DATABASE = 'db/db.sqlite'
API_KEY_AI = os.environ.get('API_KEY_AI')
TOKEN = json_data['token']
