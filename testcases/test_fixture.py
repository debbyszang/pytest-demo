# -*- coding: utf-8 -*-
# @Time : 2025/2/25 10:19
# @Author : debbyszhang
# @File : test_fixture.py
# @desc :
import pytest


@pytest.fixture(scope='class', autouse=True)
def init_browser():
    print('前置操作，初始化。。。')
    yield
    print('后置操作，关闭。。。')


@pytest.fixture(params=['apple', 'banana', 'orange', 'grape'], ids=['苹果', '香蕉', '橙子', '葡萄'], name='setup_init')
def setup(request):
    value = request.param
    return value


class TestFixture:

    def test_case_01(self):
        print('fixtrue第一个测试用例')

    def test_case_02(self):
        print('fixtrue第二个测试用例')

    def test_case_03(self, setup_init):
        print('fixtrue第三个测试用例')
        assert len(setup_init) > 0


if __name__ == '__main__':
    pytest.main(['-vs', __file__])
