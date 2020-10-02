import flask
import json 
from flask_cors import CORS


app = flask.Flask(__name__)
CORS(app, orgins="*")
app.config["DEBUG"] = True

@app.route('/',methods=['GET'])
def home():
    with open('recent.json') as f:
        data = json.load(f)
    return {'recent': data['recent']}

app.run()
