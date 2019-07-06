import requests
import json

while True:
    user = input('User? ')
    data = requests.get('https://api.scratch.mit.edu/users/' + user)
    data = data.json()
    data = data['scratchteam']
    if data == False:
        print('This user is not a member of the Scratch Team.')
    elif data == True:
        print('This user is a member of the Scratch Team')
    