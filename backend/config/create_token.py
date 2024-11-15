import string
import random
import json

def create_token(lenght):
    token = ""
    for _ in range(lenght):
        token += random.choice(string.ascii_letters)
    json_dump = {"token": token}
    with open("backend/config/token.json", "w") as json_file:
        json.dump(json_dump, json_file)
