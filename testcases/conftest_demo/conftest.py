# -*- coding: utf-8 -*-
# @Time : 2025/2/25 10:52
# @Author : debbyszhang
# @File : conftest.py
# @desc :
import pytest


@pytest.fixture(scope="function", autouse=True)
def setup():
    print('conftest_demo中前置操作，初始化。。。')
    yield
    print('conftest_demo中后置操作，关闭。。。')
