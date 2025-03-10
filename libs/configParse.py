# -*- coding: utf-8 -*-
# @Time : 2025/2/25 11:19
# @Author : debbyszhang
# @File : configParse.py
# @desc :
import configparser

from libs.mylogger import logger


class ConfigParse:
    """
    解析.ini配置文件
    """

    def __init__(self, file_path):
        self.config = configparser.ConfigParser()
        self.file_path = file_path
        self.read_config()

    def read_config(self):
        self.config.read(self.file_path)

    def get_value(self, section, option):
        try:
            value = self.config.get(section, option)
            return value
        except Exception as e:
            logger.error(f'解析配置文件出现异常，原因：{e}')


if __name__ == '__main__':
    conf = ConfigParse('../config/config.ini')
    res = conf.get_value('HOST', 'host')
    print(res)
