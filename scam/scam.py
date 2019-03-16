import requests
import os
import random
import string
import json

chars = string.ascii_letters + string.digits + 'abcdefghijklmnopqrstuvwxyz!@#$%^&*()'
random.seed = (os.urandom(1024))

url = input('Enter URL: ')
postUsername = input('Enter username form data: ')
postPassword = input('Enter password form data: ')

os.system('cls')

names = json.loads(open('names.json').read())

for name in names:
    name_extra = ''.join(random.choice(string.digits))

    username = name.lower() + name_extra + '@gmail.com'
    password = ''.join(random.choice(chars) for i in range(8))

    requests.post(url, allow_redirects = False, data = {
        postUsername: username,
        postPassword: password
    })
    print('sending username %s and password %s' % (username, password))
