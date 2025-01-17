# -*- coding: utf-8 -*-
# @Time : 2025/1/17 18:03
# @Author : debbyszhang
# @File : mylogger.py
# @desc :


import logging
import time
from logging.handlers import RotatingFileHandler

logfile_name=log_path + r'/{}.log'.format(time.strftime("%Y%m%d-%H%M%s" ))
class MyLogger(object):
    def __init__(self):
        pass

    def output(self):
        logger = logging.getLogger(__name__)
        # 防止重复打印
        if not logger.handlers:
            logger.setLevel(logging.DEBUG)
            log_format = logging.Formatter('')

            # 输出在控制台
            sh = logging.StreamHandler()
            sh.setLevel(logging.DEBUG)
            sh.setFormatter(log_format)
            logger.addHandler(sh)

            # 输出到文件
            fh = RotatingFileHandler(filename=logfile_name,mode='a',maxBytes=5242880, backupCount=5,encoding='utf-8')

