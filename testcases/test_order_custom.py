# -*- coding: utf-8 -*-
# @Time : 2025/1/17 16:07
# @Author : debbyszhang
# @File : test_case01.py
# @desc :
import pytest


class TestCase03():

    @pytest.mark.last
    def test_case4(self):
        print('case01')

    @pytest.mark.first
    def test_case5(self):
        print('case02')

    @pytest.mark.second
    def test_case6(self):
        print('case03')


if __name__ == '__main__':
    pytest.main(['-s', __file__])
