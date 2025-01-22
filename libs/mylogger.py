# -*- coding: utf-8 -*-
# @Time : 2025/1/17 18:03
# @Author : debbyszhang
# @File : mylogger.py
# @desc :


import logging
import os
import time
from logging.handlers import RotatingFileHandler

from colorlog import ColoredFormatter

from config import setting

log_path = ''
try:
    log_path = setting.FILE_PATH['log']
finally:
    # 异常处理一下
    if not os.path.exists(log_path):
        os.makedirs(log_path)
# # 异常处理一下
# if not os.path.exists(log_path):
#     os.makedirs(log_path)

logfile_name = log_path + r'/{}.log'.format(time.strftime("%Y%m%d"))
# logfile_name = log_path + r'/{}.log'.format(time.strftime("%Y%m%d%H%M%S"))


class MyLogger(object):
    def __init__(self):
        self.logger = self.output()
        pass

    def info(self, message):
        self.logger.info(message)

    def debug(self, message):
        self.logger.debug(message)

    def warning(self, message):
        self.logger.warning(message)

    def error(self, message):
        self.logger.error(message)

    @classmethod
    def color_log(cls):
        log_colors = {
            'DEBUG': 'cyan',
            'INFO': 'green',
            'WARNING': 'yellow',
            'ERROR': 'red',
            'CRITICAL': 'red,bg_white',
        }
        formatter = ColoredFormatter("%(log_color)s%(levelname)-8s %(filename)s:%(lineno)d [%(module)s:%(funcName)s] %(reset)s %(blue)s%(message)s", log_colors=log_colors)
        # formatter = ColoredFormatter("%(log_color)s%(levelname)-%(filename)s:%(lineno)d-[%(module)s:%(funcName)s]-8s%(reset)s %(blue)s%(message)s",log_colors=log_colors)
        return formatter

    def output(self):
        logger = logging.getLogger(__name__)
        stream_formatter = self.color_log()
        # 防止重复打印
        if not logger.handlers:
            logger.setLevel(logging.DEBUG)
            # log_format = logging.Formatter('')

            # 输出在控制台
            sh = logging.StreamHandler()
            sh.setLevel(logging.DEBUG)
            sh.setFormatter(stream_formatter)
            logger.addHandler(sh)

            # 输出到文件
            fh = RotatingFileHandler(filename=logfile_name, mode='a', maxBytes=5242880, backupCount=5, encoding='utf-8')
            fh.setLevel(logging.DEBUG)
            fh.setFormatter(stream_formatter)
            logger.addHandler(fh)

        return logger


logger = MyLogger()

