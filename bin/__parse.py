# -*- coding:utf8 -*-
import os
import configparser
import argparse


def __main__():
    parser = argparse.ArgumentParser()
    parser.add_argument('--config', type=str)
    options = parser.parse_args()

    ini_file = options.config
    config = configparser.ConfigParser(os.environ)
    config.read(ini_file)

    bind = config.get('server', 'bind')
    workers = config.get('server', 'workers')

    print(bind, workers)


if __name__ == '__main__':
    __main__()
