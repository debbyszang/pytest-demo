# -*- coding: utf-8 -*-
# @Time : 2025/1/17 16:07
# @Author : debbyszhang
# @File : test_case01.py
# @desc :
import pytest


class TestSetupTeardown:

    @classmethod
    def setup_class(cls):
        print('setupXXXXXXX...')

    def test_case4(self):
        print('case4...')

    def test_case5(self):
        print('case5...')

    @classmethod
    def teardown_class(cls):
        print('teardownXXXXXX...')


if __name__ == '__main__':
    pytest.main(['-vs', __file__])
