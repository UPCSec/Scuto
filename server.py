from scuto import app
from scuto import config
from aiohttp import web


if __name__ == '__main__':
    web.run_app(app,
                host=config.deep_get('Scuto.host', default='0.0.0.0'),
                port=config.deep_get('Scuto.port', default=8086))