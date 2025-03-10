# -*- coding: utf-8 -*-
# @Time : 2025/2/25 10:43
# @Author : debbyszhang
# @File : test_conftest_fixure.py
# @desc :
import pytest


class TestFixture:

    def test_case_01(self):
        print('conf  fixtrue第一个测试用例')

    def test_case_02(self):
        print('conf  fixtrue第二个测试用例')


if __name__ == '__main__':
    pytest.main(['-vs', __file__])
