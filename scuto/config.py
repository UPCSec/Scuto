import json

config = {}

with open('scuto/config.json') as conf:
    conf = json.load(conf)
    for k in conf:
        config[k] = conf[k]
