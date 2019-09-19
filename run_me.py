import ast
import time
import random
import requests
from stem import Signal
from bs4 import BeautifulSoup
from stem.control import Controller
from itertools import cycle

RANDOM_MODE = True

def get_tor_session():
    session = requests.session()
    session.proxies = {'http': 'socks5://127.0.0.1:9050',
                       'https': 'socks5://127.0.0.1:9050'}
    return session

def get_random_header():
    headers = {}
    with open('user-agents.txt') as arq:
        content_list = arq.readlines()
    idx = random.randint(0, len(content_list))
    headers['User-agent'] = content_list[idx].replace('\n','')
    return headers

def change_ip():
    with Controller.from_port(port = 9051) as controller:
        controller.authenticate(password='henrique')
        controller.signal(Signal.NEWNYM)
    print('Ip changed')

while True:

    session = get_tor_session()
    session.headers.update(get_random_header())
    
    if RANDOM_MODE:
        MAX_REQUESTS = range(random.randint(200,350))
        print('Making', MAX_REQUESTS.stop, 'requests')
    else:
        MAX_REQUESTS = cycle([0])

    for i in MAX_REQUESTS:
        
        page = session.get('<URL_TO_TEST>')
        uag = session.get('https://httpbin.org/user-agent')
        ipp = session.get('https://httpbin.org/ip')
        ip = ast.literal_eval(ipp.text)['origin'].split(', ')[0]
        ua = ast.literal_eval(uag.text)['user-agent'].replace(' ','')
        
        content = BeautifulSoup(page.content, 'html.parser').find_all('<TAG_TO_FIND>')
        
        if len(content) == 0:
            print(ip, 'blocked. Getting new IP')
            break
        t_list = [c.text for c in content]
    
        sleep_time = 0#random.randint(1,4)
        print("[{}] {} ({}) Response lenght:{} (Sleep...{})".format(ipp.status_code, ip, ua, len(t_list), sleep_time))

    change_ip()
