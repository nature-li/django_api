# -*- coding:utf8 -*-
from config.config import Config
from mt_log import AsyncLogger
from mt_log import SyncLogger

Logger = None

if Config.LOG_ASYNC:
    Logger = AsyncLogger
else:
    Logger = SyncLogger
