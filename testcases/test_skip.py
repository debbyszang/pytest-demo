# -*- coding: utf-8 -*-
# @Time : 2025/1/17 16:07
# @Author : debbyszhang
# @File : test_case01.py
# @desc :
import pytest


class TestCase03():

    @pytest.mark.skip(reason="Not implemented")
    def test_case4(self):
        print('case skip')

    sum = 5
    @pytest.mark.skipif(condition=(sum > 3), reason="no condition")
    def test_case5(self):
        print('case skip if')

    def test_case6(self):
        print('case...')


if __name__ == '__main__':
    pytest.main(['-vs', __file__])
