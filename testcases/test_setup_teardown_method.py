# -*- coding: utf-8 -*-
# @Time : 2025/1/17 16:07
# @Author : debbyszhang
# @File : test_case01.py
# @desc :
import pytest


class TestSetupTeardown:

    def setup_method(self, method):
        print('setupXXXXXXX...')

    def test_case4(self):
        print('case4...')

    def test_case5(self):
        print('case5...')

    def teardown_method(self, method):
        print('teardownXXXXXX...')


if __name__ == '__main__':
    pytest.main(['-vs', __file__])
