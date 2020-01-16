from flask import Flask, request
from scuto.models import init_mongodb
from scuto.api.v1 import register_apis
import json


app = Flask('scuto')
app.__version__ = "0.0.1"
with open('scuto/config.json') as conf:
    conf = json.load(conf)
    for k in conf:
        app.config[k.upper()] = conf[k]
db = init_mongodb(app)
register_apis(app)
