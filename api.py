import flask
import json 
import requests
from flask_cors import CORS


app = flask.Flask(__name__)
CORS(app, orgins="*")
app.config["DEBUG"] = True

@app.route('/',methods=['GET'])
def home():
    f = requests.get('https://tools.airfire.org/websky/v1/api/runs/standard/GFS-0.15deg/')
    url = f.json()['run_urls'][0]
    return {'recent': url}

@app.route('/fast',methods=['GET'])
def fast():
    with open('recent.json') as f:
        data = json.load(f)
    return {'recent': data['recent']}
app.run()
