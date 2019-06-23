import urllib.request
import json

print('What is your Scratch username?')
username = input('Username: ')
print('Have some stats')

print('BASIC DATA')
response = urllib.request.urlopen('https://api.scratch.mit.edu/users/' + username).read()
parsed = json.loads(response)
print(json.dumps(parsed, indent=4))

print('FOLLOWER DATA')
followers_response = urllib.request.urlopen('https://api.scratch.mit.edu/users/' + username + '/followers').read()
followers_parsed = json.loads(followers_response)
print(json.dumps(followers_parsed, indent=4))

print('FOLLOWING DATA')
following_response = urllib.request.urlopen('https://api.scratch.mit.edu/users/' + username + '/following').read()
following_parsed = json.loads(following_response)
print(json.dumps(following_parsed, indent=4))

print('MESSAGE DATA')
message_response = urllib.request.urlopen('https://api.scratch.mit.edu/users/' + username + '/messages/count').read()
message_parsed = json.loads(message_response)
print(json.dumps(message_parsed, indent=4))

print('FAVOURITE DATA')
favourites_response = urllib.request.urlopen('https://api.scratch.mit.edu/users/' + username + '/favorites').read()
favourites_parsed = json.loads(favourites_response)
print(json.dumps(favourites_parsed, indent=4))

print('PROJECTS DATA')
projects_response = urllib.request.urlopen('https://api.scratch.mit.edu/users/' + username + '/projects').read()
projects_parsed = json.loads(projects_response)
print(json.dumps(projects_parsed, indent=4))
