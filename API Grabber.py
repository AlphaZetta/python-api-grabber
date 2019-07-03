import requests
import json
while True:
    print('Input an API URL')
    url = input()
    
    response = requests.get(url)
    parsed = response.json()
    
    print(json.dumps(parsed, indent=4))
