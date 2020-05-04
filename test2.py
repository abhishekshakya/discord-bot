from phlib import PornHub
import random
import requests
import json

with open('token.json','r') as openfile:
    token = json.load(openfile)

print(token['token'])