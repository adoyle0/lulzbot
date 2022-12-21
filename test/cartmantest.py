import requests
import json

url = 'https://doordesk.net/chat'

active = True

while active:
    user_input = input('>> ')
    if user_input in 'q':
        active = False
        break
    message = {'Message': user_input}
    response = requests.post(url,json.dumps(message))
    print(response.json().get('Cartman'))
