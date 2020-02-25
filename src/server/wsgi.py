"""
WSGI config for server project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/howto/deployment/wsgi/
"""

import os
from django.core.handlers.wsgi import WSGIHandler
from config.config import Config
from . import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'server.settings')


class Application(WSGIHandler):
    def __init__(self, *args, **kwargs):
        super(WSGIHandler, self).__init__(*args, **kwargs)
        self.logger = Logger

    def stop_logger(self):
        if self.logger:
            self.logger.stop()


ini_path = os.environ['APP_INI']
if Config.init(ini_path):
    from log.logger import Logger
    Logger.start(Config.LOG_ENV, Config.LOG_TARGET, Config.LOG_NAME, Config.LOG_SIZE,
                 Config.LOG_COUNT, settings.LOCKER)
    application = Application()
else:
    application = None
