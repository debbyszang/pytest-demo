# -*- coding: utf-8 -*-
# @Time : 2025/1/17 16:07
# @Author : debbyszhang
# @File : test_case01.py
# @desc :
import pytest


class TestCase03():

    @pytest.mark.xfail
    def test_case4(self):
        print('case xfail')

    sum = 5
    def test_case5(self):
        print('case 05')

    def test_case6(self):
        print('case...')


if __name__ == '__main__':
    pytest.main(['-vs', __file__])
