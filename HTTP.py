import requests
import json

method = 'global'

print('Say .help for more info')

while True:
    if method == 'global':
        ans = input('> ')
    elif method == 'native':
        ans = input(website + '/> ')
    
    if ans == '.help':
        print('Say .help for help')
        print('Say .global for global data')
        print('Say .native for one website')
    elif ans == '.global':
        method = 'global'
        print()
    elif ans == '.native':
        method = 'native'
        print('What website?')
        website = input()
        print()
    elif ans[:3] == 'GET':
        if method == 'global':
            data = requests.get(ans[4:])
            if data.status_code != 200:
                print('Website not recognised')
                print()
                continue
            data = data.json()
            print(json.dumps(data, indent=4))
            print()
        elif method == 'native':
            r = website + ans[4:]
            data = requests.get(r)
            if data.status_code != 200:
                print('Website not recognised')
                print()
                continue
            data = data.json()
            print(json.dumps(data, indent=4))
            print()
    else:
        print('Request and/or command was not recognised, please try again')
        print()
