# -*- coding: utf-8 -*-
# @Time : 2025/1/17 16:07
# @Author : debbyszhang
# @File : test_case01.py
# @desc :
import os
import shutil

import allure
import pytest


@allure.feature('测试类')
class TestCase03():

    @pytest.mark.parametrize('params', ['python', 'java', 'c#'])
    def test_case4(self, params):
        print(params)

    sum = 5

    @allure.story('测试用例01')
    @allure.title('验证case01成功')
    @allure.description('描述：随便测试一下')
    @allure.severity(allure.severity_level.MINOR)
    def test_case5(self):
        print('case 05')

    def test_case6(self):
        print('case...')

    def test_case7(self):
        print('case7...')


if __name__ == '__main__':
    # pytest.main(['-vs', '--alluredir=./result/tmp', __file__])
    pytest.main(['-vs', '--alluredir=./result/tmp', '--clean-alluredir', __file__])

    # pytest.main(['-s', __file__])
    shutil.copy('../environment.xml', './result/tmp')
    pytest.main(['-vs', '--alluredir=./result/tmp', __file__])
    # pytest.main(['-vs', '--alluredir=./result/tmp', '--clean-alluredir', __file__])

    # 离线报告
    os.system('allure generate  ./result/tmp -o ./result/offline --clean')

    # 在线报告
    os.system('allure serve  ./result/tmp')
