# -*- coding: utf-8 -*-
# @Time : 2025/1/17 18:14
# @Author : debbyszhang
# @File : setting.py
# @desc :
import os
import sys

PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(PROJECT_ROOT)

print(PROJECT_ROOT)

# 可定义多个文件路径
FILE_PATH = {
    'log': os.path.join(PROJECT_ROOT, 'logs'),
    'ini': os.path.join(PROJECT_ROOT, 'config', 'config.ini')
}

print(FILE_PATH['log'])
print(FILE_PATH['ini'])

print(FILE_PATH['log'])
if not os.path.exists(FILE_PATH['log']):
    os.makedirs(FILE_PATH['log'])
if not os.path.exists(FILE_PATH['report']):
    os.makedirs(FILE_PATH['report'])
