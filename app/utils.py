from app.exceptions import InvalidInput
import os, json

def import_cvdata(path: str):
    data = '' 
    if not os.path.isfile(path):
        raise InvalidInput

    with open(path, 'r') as file:
        data = json.load(file)
    return data