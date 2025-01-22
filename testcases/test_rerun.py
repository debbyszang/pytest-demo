# -*- coding: utf-8 -*-
# @Time : 2025/1/17 16:07
# @Author : debbyszhang
# @File : test_case01.py
# @desc :
import pytest


class TestCase02():

    def test_case4(self):
        assert True

    # @pytest.mark.flaky(reruns=3, reruns_delay=2)
    def test_case5(self):
        assert False

    def test_case6(self):
        assert True


if __name__ == '__main__':
    pytest.main(['-s', '--reruns=3', __file__])
