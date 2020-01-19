from aiohttp.web import middleware, json_response
from scuto.config import config
import logging


async def log_error(error: Exception):
    logger = logging.getLogger('aiohttp.server')
    logger.exception(error)

@middleware
async def error_info(request, handler):
    """
    Hide 500 error info if debug is not set.
    """
    error = {
        'error': 'The server responds with an error.'
    }
    try:
        resp = await handler(request)
        if resp.status == 500 and config.get('Scuto.debug'):
            await log_error(e)
        else:
            return resp
    except Exception as e:
        await log_error(e)
    return json_response(error, status=500)