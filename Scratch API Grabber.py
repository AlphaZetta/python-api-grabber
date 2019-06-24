import urllib.request
import json

print('Only put everything after \'api.scratch.mit.edu/\'')

while True:
    url = input()
    response = urllib.request.urlopen('https://api.scratch.mit.edu/' + url).read()
    parsed = json.loads(response)
      
    print(json.dumps(parsed, indent=4))
