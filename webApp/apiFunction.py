import json
import ndjson
import requests
from click import clear

clear()

def getDog():

    api_endpoint = "https://dog.ceo/api/breeds/image/random"
    response = requests.get(
        api_endpoint
    )

    dogPicsJson = []

    for jsonObj in response:
        dogPicsDict = json.loads(jsonObj)
        dogPicsJson.append(dogPicsDict)


    return dogPicsJson