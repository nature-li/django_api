import os
import configparser


class Config(object):
    def __init__(self):
        # server
        self.server_listen = ''
        self.server_debug = False
        # kafka
        self.kafka_address = ''
        self.kafka_topic = ''
        # zookeeper
        self.zk_address = ''
        self.zk_root = ''
        # mysql
        self.mysql_host = ''
        self.mysql_port = 0
        self.mysql_user = ''
        self.mysql_pwd = ''
        self.mysql_db = ''

    def __load(self):
        path_file = os.path.abspath(__file__)
        # print(path_file)
        path_server = os.path.dirname(path_file)
        # print(path_server)
        path_src = os.path.dirname(path_server)
        # print(path_src)
        path_project = os.path.dirname(path_src)
        # print(path_project)
        path_conf = os.path.join(path_project, 'conf')
        # print(path_conf)
        path_ini = os.path.join(path_conf, 'config.ini')
        # print(path_ini)

        config = configparser.ConfigParser(os.environ)
        config.read(path_ini)

        # wsgi
        self.server_listen = config.get('wsgi', 'bind', raw=True)
        self.server_debug = config.getboolean('wsgi', 'reload', raw=True)

    def __overwrite_global(self):
        global bind
        bind = self.server_listen
        global reload
        reload = self.server_debug

    def init(self):
        self.__load()
        self.__overwrite_global()


'''
=======================[wsgi 默认配置]========================
'''
# 监听内网端口
bind = None
# 是否自动拉起
reload = None

'''
=======================[]========================
'''
# 加载用户配置
__setting = Config()
__setting.init()


