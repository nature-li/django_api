# -*- coding:utf8 -*-
import os
import configparser
import traceback
import urllib.parse


class Config(object):
    # SERVER
    SERVER_BIND = ''
    SERVER_WORKERS = 1
    # MYSQL
    MYSQL_HOST = '127.0.0.1'
    MYSQL_PORT = 3306
    MYSQL_USER = ''
    MYSQL_PWD = ''
    MYSQL_DB = 'exp_platform'
    MYSQL_URI = ''
    # ZOOKEEPER
    ZOOKEEPER_HOST = ''
    ZOOKEEPER_ROOT = ''
    # KAFKA
    KAFKA_HOST = ''
    KAFKA_TOPIC = ''
    # LOG
    LOG_ENV = None
    LOG_TARGET = ''
    LOG_NAME = ''
    LOG_SIZE = 100 * 1024 * 1024
    LOG_COUNT = 100
    LOG_ASYNC = False

    @classmethod
    def log_config(cls, logger):
        try:
            for k, v in cls.__dict__.items():
                if not k.startswith('__'):
                    if not callable(getattr(cls, k)):
                        content = '%s := %s' % (k, v)
                        logger.info(content)
        except:
            print(traceback.format_exc())

    @classmethod
    def init(cls, ini_file):
        try:
            config = configparser.ConfigParser(os.environ)
            config.read(ini_file)
            # SERVER
            cls.SERVER_BIND = config.get('server', 'bind', raw=True)
            cls.SERVER_WORKERS = config.getint('server', 'workers', raw=True)
            # MYSQL
            cls.MYSQL_HOST = config.get('mysql', 'host', raw=True)
            cls.MYSQL_PORT = config.get('mysql', 'port', raw=True)
            cls.MYSQL_USER = config.get('mysql', 'user', raw=True)
            cls.MYSQL_PWD = config.get('mysql', 'pwd', raw=True)
            cls.MYSQL_DB = config.get('mysql', 'db', raw=True)
            cls.MYSQL_URI = 'mysql://%s:%s@%s/%s?charset=utf8' % \
                            (cls.MYSQL_USER, urllib.parse.quote(cls.MYSQL_PWD), cls.MYSQL_HOST, cls.MYSQL_DB)
            # ZOOKEEPER
            cls.ZOOKEEPER_HOST = config.get('zookeeper', 'host', raw=True)
            cls.ZOOKEEPER_ROOT = config.get('zookeeper', 'root', raw=True)
            # KAFKA
            cls.KAFKA_HOST = config.get('kafka', 'host', raw=True)
            cls.KAFKA_TOPIC = config.get('kafka', 'topic', raw=True)
            # LOG
            cls.LOG_ENV = config.get('log', 'environment', raw=True)
            cls.LOG_TARGET = config.get('log', 'target')
            cls.LOG_NAME = config.get('log', 'file_name', raw=True)
            cls.LOG_SIZE = config.getint('log', 'file_size', raw=True)
            cls.LOG_COUNT = config.getint('log', 'file_count', raw=True)
            cls.LOG_COUNT = config.getboolean('log', 'async', raw=True)
            return True
        except:
            print(traceback.format_exc())
