from functools import reduce
import json


class Config(dict):
    def deep_get(self, deep_key, default=None):
        return reduce(lambda conf, key: conf.get(key, default) if isinstance(conf, dict) else default, deep_key.split('.'), self)

config = Config()
config.app_version = "0.0.1"

with open('scuto/config.json') as conf:
    config.update(json.load(conf))
