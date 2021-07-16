import requests
import os
import random
import string
import json
import threading

chars = string.ascii_letters + string.digits + 'abcdefghijklmnopqrstuvwxyz!@#$%^&*()'
random.seed = (os.urandom(1024))

url = input('Enter URL: ')
postEmail = input('Enter email form data: ')
postPassword = input('Enter password form data: ')
threadsAmount = int(input('Enter amount of threads: '))

os.system('cls')

names = json.loads(open('names.json').read())

def request():
    for name in names:
        name_extra = ''.join(random.choice(string.digits))

        email = name.lower() + name_extra + '@gmail.com'
        password = ''.join(random.choice(chars) for i in range(8))

        requests.post(url, allow_redirects = False, data = {
            postEmail: email,
            postPassword: password
        })
        print('sending email %s and password %s' % (email, password))

threads = []

for i in range(threadsAmount):
    t = threading.Thread(target=request)
    t.daemon = True
    threads.append(t)

for i in range(threadsAmount):
    threads[i].start()

for i in range(threadsAmount):
    threads[i].join()
