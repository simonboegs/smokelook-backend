import requests
import json

print('running update.py')
f = requests.get('https://tools.airfire.org/websky/v1/api/runs/standard/GFS-0.15deg/')
url = f.json()['run_urls'][0]

with open('recent.json','w') as json_file:
    json.dump({'recent': url}, json_file)
