import requests
import json

print('What is your Scratch username?')
username = input('Username: ')
print('Have some stats')

print('BASIC DATA')
response = requests.get('https://api.scratch.mit.edu/users/' + username)
parsed = response.json()
print(json.dumps(parsed, indent=4))

print('FOLLOWER DATA')
followers_response = requests.get('https://api.scratch.mit.edu/users/' + username + '/followers')
followers_parsed = followers_response.json()
print(json.dumps(followers_parsed, indent=4))

print('FOLLOWING DATA')
following_response = requests.get('https://api.scratch.mit.edu/users/' + username + '/following')
following_parsed = following_response.json()
print(json.dumps(following_parsed, indent=4))

print('MESSAGE DATA')
message_response = requests.get('https://api.scratch.mit.edu/users/' + username + '/messages/count')
message_parsed = message_response.json()
print(json.dumps(message_parsed, indent=4))

print('FAVOURITE DATA')
favourites_response = requests.get('https://api.scratch.mit.edu/users/' + username + '/favorites')
favourites_parsed = favourites_response.json()
print(json.dumps(favourites_parsed, indent=4))

print('PROJECTS DATA')
projects_response = requests.get('https://api.scratch.mit.edu/users/' + username + '/projects')
projects_parsed = projects_response.json()
print(json.dumps(projects_parsed, indent=4))
