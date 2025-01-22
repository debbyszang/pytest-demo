# -*- coding: utf-8 -*-
# @Time : 2025/1/17 16:07
# @Author : debbyszhang
# @File : test_case01.py
# @desc :
import pytest


class TestCase03():

    @pytest.mark.P1
    def test_case4(self):
        print('case P1')

    @pytest.mark.P2
    def test_case5(self):
        print('case P2')

    def test_case6(self):
        print('case...')


if __name__ == '__main__':
    # pytest.main(['-s', '-m P1', __file__])
    # pytest.main(['-s', '-m P1 or P2', __file__])
    pytest.main(['-s', __file__])
