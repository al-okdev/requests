import requests
from pprint import pprint
import json
from operator import itemgetter

TOKEN = '2619421814940190'

API_BASE_URL = "https://superheroapi.com/api/"

list_superhero = ['Hulk', 'Captain America', 'Thanos']

list_superhero_intelligence = []

for item_superhero in list_superhero:
    superhero_dict = {}
    r = requests.get(API_BASE_URL + TOKEN + '/search/' + item_superhero)
    result_json = int(r.json()['results'][0]['powerstats']['intelligence'])

    superhero_dict['name'] = item_superhero
    superhero_dict['intelligence'] = result_json

    list_superhero_intelligence.append(superhero_dict)


list_superhero_intelligence = sorted(list_superhero_intelligence, key=itemgetter('intelligence'), reverse=True)
max_intelligence_superhero = list_superhero_intelligence[0]['name']
print(f'Самый умный супергерой: {max_intelligence_superhero}')
