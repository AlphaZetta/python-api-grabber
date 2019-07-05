import requests
import json

def api(url):
    response = requests.get(url)
    parsed = response.json()

    print(json.dumps(parsed, indent=4))
