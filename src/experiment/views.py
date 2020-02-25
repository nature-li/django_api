from django.shortcuts import render
from django.http import HttpResponse
import json
import logging
import os
import multiprocessing
import threading
from django.conf import settings
from server.logger import Logger


logger = logging.getLogger(__name__)


# Create your views here.
def index(request):
    # print('<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<')
    Logger.info("This is a info message.")
    # print("This is a info message.")
    # settings.LOCKER.acquire()
    # print(os.getpid(), id(settings.LOCKER))
    # settings.LOCKER.release()
    # for k, v in settings.LYG_CONFIG:
    #     print(k)
    #     print(v)
    #     print('-------------------------')
    # print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
    # settings.LOCKER.acquire()
    # print(os.getpid(), threading.current_thread().ident)
    # settings.LOCKER.release()
    return HttpResponse("Hello, world. You're at the polls index. {}:{}".format(os.getpid(), threading.current_thread().ident))
