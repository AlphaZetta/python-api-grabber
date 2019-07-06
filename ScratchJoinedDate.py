import requests
import json

while True:
    user = input('What user? ')
    data = requests.get('https://api.scratch.mit.edu/users/' + user)
    data = data.json()
    data = data['history']['joined']

    data = data[:-14]
    data_year = data[0:4]
    data_date = data[-2:]
    data_month = data[-5:-3]

    if data_date[-1:] != 1 or 2 or 3:
        data_date = data_date + 'th'
    elif data_date[-1:] == 1:
        data_date = data_date + 'st'
    elif data_date[-1:] == 2:
        data_date = data_date + 'nd'
    elif data_date[-1:] == 3:
        data_date = data_date + 'rd'

    if data_date[:1] == '0':
        data_date = data_date[1:]
    
    if data_month == '01':
        data_month = 'January'
    elif data_month == '02':
        data_month = 'February'
    elif data_month == '03':
        data_month = 'March'
    elif data_month == '04':
        data_month = 'April'
    elif data_month == '05':
        data_month = 'May'
    elif data_month == '06':
        data_month = 'June'
    elif data_month == '07':
        data_month = 'July'
    elif data_month == '08':
        data_month = 'August'
    elif data_month == '09':
        data_month = 'September'
    elif data_month == '10':
        data_month = 'October'
    elif data_month == '11':
        data_month = 'November'
    elif data_month == '12':
        data_month = 'December'
    
    print('Joined ' + data_month + ' the ' + data_date + ' ' + data_year)
