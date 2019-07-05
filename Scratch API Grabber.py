import requests
import json

print('Only put everything after \'api.scratch.mit.edu/\'')

while True:
    url = input()
    response = requests.get('https://api.scratch.mit.edu/' + url)
    parsed = response.json()
      
    print(json.dumps(parsed, indent=4))
