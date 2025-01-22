# -*- coding: utf-8 -*-
# @Time : 2025/1/17 16:07
# @Author : debbyszhang
# @File : test_case01.py
# @desc :
from time import sleep

import pytest

from libs.mylogger import logger


class TestCase01():

    def test_case1(self):
        logger.info("ssss")
        sleep(2)
        assert True

    def test_case2(self):
        sleep(2)

        assert True

    def test_case3(self):
        sleep(2)

        assert True


if __name__ == '__main__':
    pytest.main(["-s", __file__])
    # pytest.main(["-n 3", __file__])