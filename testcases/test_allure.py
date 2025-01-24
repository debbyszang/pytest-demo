# -*- coding: utf-8 -*-
# @Time : 2025/1/17 16:07
# @Author : debbyszhang
# @File : test_case01.py
# @desc :
import json
import os
import shutil
from time import time

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

    @pytest.mark.xfail(reason='aaa')
    def test_case6(self):
        print('case...')

    @pytest.mark.skip(reason='bbb')
    def test_case7(self):
        print('case7...')
        assert 1 == 3

    def test_case7(self):
        print('case7...')
        assert 1 == 3

# 对生成的Allure报告进行进一步演进（生成一个相对独立的报告静态工程）
# ALLURE_PLUS_DIR 是存放要生成的报告
# buildOrder 是表示以构建次数为文件夹名称
# command = f"allure generate {ALLURE_PATH} -o {os.path.join(ALLURE_PLUS_DIR,str(buildOrder))} --clean"
# os.system(command)
def get_dirname(ALLURE_PLUS_DIR):
    hostory_file = os.path.join(ALLURE_PLUS_DIR, "history.json")
    if os.path.exists(hostory_file):
        with open(hostory_file) as f:
            li = eval(f.read())
        # 根据构建次数进行排序，从大到小
        li.sort(key=lambda x: x['buildOrder'], reverse=True)
        # 返回下一次的构建次数，所以要在排序后的历史数据中的buildOrder+1
        return li[0]["buildOrder"]+1, li
    else:
        # 首次进行生成报告，肯定会进到这一步，先创建history.json,然后返回构建次数1（代表首次）
        with open(hostory_file, "w") as f:
            pass
        return 1, None


def update_trend_data(dirname, allure_url,ALLURE_PLUS_DIR, old_data: list):
    """ dirname：构建次数 old_data：备份的数据 update_trend_data(get_dirname()) """
    WIDGETS_DIR = os.path.join(ALLURE_PLUS_DIR, f"{str(dirname)}/widgets")
    # 读取最新生成的history-trend.json数据
    with open(os.path.join(WIDGETS_DIR, "history-trend.json")) as f:
        data = f.read()

    new_data = eval(data)
    if old_data is not None:
        new_data[0]["buildOrder"] = old_data[0]["buildOrder"]+1
    else:
        old_data = []
        new_data[0]["buildOrder"] = 1
    # 给最新生成的数据添加reportUrl key，reportUrl要根据自己的实际情况更改
    new_data[0]["reportUrl"] = f"{allure_url}/{dirname}/index.html"
    # 把最新的数据，插入到备份数据列表首位
    old_data.insert(0, new_data[0])
    # 把所有生成的报告中的history-trend.json都更新成新备份的数据old_data，这样的话，点击历史趋势图就可以实现新老报告切换
    for i in range(1, dirname+1):
        with open(os.path.join(ALLURE_PLUS_DIR, f"{str(i)}/widgets/history-trend.json"), "w+") as f:
            f.write(json.dumps(old_data))
    # 把数据备份到history.json
    hostory_file = os.path.join(ALLURE_PLUS_DIR, "history.json")
    with open(hostory_file, "w+") as f:
        f.write(json.dumps(old_data))
    return old_data, new_data[0]["reportUrl"]


if __name__ == '__main__':
    ALLURE_DIR = os.path.dirname(__file__)
    print(ALLURE_DIR)
    ALLURE_PATH = os.path.join(ALLURE_DIR, str(int(time())))
    # command = f'pytest {BASEDIR} -s --alluredir={ALLURE_PATH}'
    # os.system(command)
    # pytest.main(['-vs', '--alluredir=./result/tmp', __file__])
    pytest.main(['-vs', '--alluredir=./result/tmp', '--clean-alluredir', __file__])

    # pytest.main(['-s', __file__])
    shutil.copy('../allure_reports/environment.xml', './result/tmp')
    shutil.copy('../allure_reports/categories.json', './result/tmp')
    shutil.copy('../allure_reports/history-trend.json', './result/tmp')
    pytest.main(['-vs', '--alluredir=./result/tmp', __file__])
    # pytest.main(['-vs', '--alluredir=./result/tmp', '--clean-alluredir', __file__])

    # 离线报告
    os.system('allure generate  ./result/tmp -o ./result/offline --clean')

    # 在线报告
    os.system('allure serve  ./result/tmp')

    # ALLURE_PATH = os.path.join(ALLURE_DIR, str(int(time())))
    # command = f'pytest {BASEDIR} -s --alluredir={ALLURE_PATH}'
    # os.system(command)
    # # 先调用get_dirname()，获取到这次需要构建的次数
    # buildOrder, old_data = get_dirname()
    # # 再执行命令行
    # command = f"allure generate {ALLURE_PATH} -o {os.path.join(ALLURE_PLUS_DIR, str(buildOrder))} --clean"
    # os.system(command)
    # # 执行完毕后再调用update_trend_data()
    # all_data, reportUrl = update_trend_data(buildOrder, old_data)
