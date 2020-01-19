from scuto.config import config
from scuto.util.decorators import asynchronos
from scuto.util.time import now
import logging

@asynchronos
def setup_logging(app):
    log_level = logging.__dict__[config.deep_get('Scuto.log_level')]
    logging.basicConfig(level=log_level)
    for logger_name in config.deep_get('Scuto.loggers'):
        logger = logging.getLogger(logger_name)
        logger.propagate = False
        file_handler = logging.FileHandler(f"{config.deep_get('Scuto.log_directory')}/{logger_name}.log", mode='a+')
        file_handler.setLevel(log_level)
        logger.addHandler(file_handler)
    return app

def log_activity(activity, ip):
    logger = logging.getLogger('scuto')
    logger.debug(f'{now()} - {ip} - activity')