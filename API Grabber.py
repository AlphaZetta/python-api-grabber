import urllib.request
import json

def api(url):
    response = urllib.request.urlopen(url).read()
    parsed = json.loads(response)
    
    print(json.dumps(parsed, indent=4))
