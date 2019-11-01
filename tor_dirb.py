
"""
KIMERA
"""

import sys
import ast
import random
import requests
from stem import Signal
from bs4 import BeautifulSoup
from stem.control import Controller
from itertools import cycle
import time
import urllib.parse

MAX_TIMEOUT = 3 #seconds
URL = sys.argv[1]
DIRS_FILE = sys.argv[2]
AGENTS_FILE = sys.argv[3]

EXIST_DIR_FILE = []
DIR_LIST = []
with open(DIRS_FILE, 'r') as arq:
    for line in arq.readlines():
        if line is not '\n':
            line = line.replace('\n','')
            DIR_LIST.append(line)
random.shuffle(DIR_LIST)

def get_tor_session():
    session = requests.session()
    session.proxies = {'http': 'socks5://127.0.0.1:9050','https': 'socks5://127.0.0.1:9050'}
    return session

def get_random_header():
    headers = {}
    with open(AGENTS_FILE) as arq:
        content_list = arq.readlines()
    idx = random.randint(0, len(content_list))
    headers['User-agent'] = content_list[idx].replace('\n','')
    return headers

def change_ip():
    with Controller.from_port(port = 9051) as controller:
        controller.authenticate(password='henrique')
        controller.signal(Signal.NEWNYM)
    print_ip()

def print_ip():
    ipp = SESSION.get('https://httpbin.org/ip', timeout=MAX_TIMEOUT)
    ip = ast.literal_eval(ipp.text)['origin'].split(', ')[0]
    print('Current ip:', ip)


SESSION = get_tor_session()
SESSION.headers.update(get_random_header())
print_ip()

while True:
    
    try:
        for dir in DIR_LIST:
            url_to_test = urllib.parse.urljoin(URL, dir)
            target      = SESSION.get(url_to_test, timeout=MAX_TIMEOUT)
            code       = target.status_code
            code_group = int(str(code)[0])

            if code == 403:
                change_ip()

            if code_group == 2 or code_group == 3:
                EXIST_DIR_FILE.append(url_to_test)
                print('[{}] {}'.format(target.status_code, url_to_test))

    except KeyboardInterrupt:
        break
    except Exception as e:
        print(format(e), type(e))
        break

print('\n')
for i in EXIST_DIR_FILE:
    print('[FOUND]', i)

