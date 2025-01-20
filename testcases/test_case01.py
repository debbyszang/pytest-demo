# -*- coding: utf-8 -*-
# @Time : 2025/1/17 16:07
# @Author : debbyszhang
# @File : test_case01.py
# @desc :
from libs.mylogger import logger


class TestCase01():

    def test_case1(self):
        logger.info("ssss")
        assert True

    def test_case2(self):
        assert False

    def test_case3(self):
        assert True


