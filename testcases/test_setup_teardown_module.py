# -*- coding: utf-8 -*-
# @Time : 2025/1/17 16:07
# @Author : debbyszhang
# @File : test_case01.py
# @desc :
import pytest


def setup_module():
    print("setup_module: Setup state for the entire module")


def teardown_module():
    print("teardown_module: Teardown state for the entire module")


def test_case1():
    print("test_case1: Running test")
    assert True


def test_case2():
    print("test_case2: Running test")
    assert True


if __name__ == '__main__':
    pytest.main(['-vs', __file__])
