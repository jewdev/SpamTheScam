import requests
import os
import random
import string
import json

chars = string.ascii_letters + string.digits + 'abcdefghijklmnopqrstuvwxyz'
random.seed = (os.urandom(1024))

url = 'https://www.bluemalgeran.xyz'

names = json.loads(open('names.json').read())

for name in names:
    name_extra = ''.join(random.choice(string.digits))

    username = name.lower() + name_extra + '@gmail.com'
    password = ''.join(random.choice(chars) for i in range(8))

    requests.post(url, allow_redirects = True, data = {
        'LoginForm[username]': username,
        'LoginForm[password]': password
    })
    print("sending username %s and password %s" % (username, password))