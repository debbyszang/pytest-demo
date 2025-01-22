# -*- coding: utf-8 -*-
# @Time : 2025/1/17 16:07
# @Author : debbyszhang
# @File : test_case01.py
# @desc :
import pytest


class TestSetupTeardown:

    @pytest.fixture(autouse=True)
    def setup_teardown(self):
        print('setupXXXXXXX...')
        yield
        print('teardownXXXXXX...')

    def test_case4(self):
        print('case4...')


if __name__ == '__main__':
    pytest.main(['-vs', __file__])
