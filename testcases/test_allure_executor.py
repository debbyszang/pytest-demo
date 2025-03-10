# -*- coding: utf-8 -*-
# @Time : 2025/1/17 16:07
# @Author : debbyszhang
# @File : test_case01.py
# @desc :
import ast
import json
import os
import platform
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

    def test_case8(self):
        print('case7...')
        assert 1 == 3

    def test_case9(self):
        print('case7...')
        assert 3 == 3

    def test_case10(self):
        print('case7...')
        assert 3 == 3


# 需要执行的测试脚本的路径
test_path = "./test_allure_trend.py"
# 需要生成的xml的路径起
allure_xml_path = "../allure_reports/allure_xml/"
# 需要生成测试报告的路径
allure_path = "../allure_reports/allure_report"


# 获取下一个文件夹的名称，以及最近一个趋势的数据

def set_report_env_on_results():
    """
    在allure-results报告的目录下生成一个写入了环境信息的文件：environment.properties(注意：不能放置中文，否则会出现乱码)
    @return:
    """
    # 需要写入的环境信息
    allure_env = {
        'OperatingEnvironment': '测试环境',
        'BaseUrl': 'www.baidu.com',
        'PythonVersion': platform.python_version(),
        'Platform': platform.platform(),
        'PytestVersion': pytest.__version__,
    }
    xml_path = os.path.join(allure_xml_path, str(buildOrder))
    allure_env_file = os.path.join(xml_path, 'environment.xml')
    with open(allure_env_file, 'w', encoding='utf-8') as f:
        for _k, _v in allure_env.items():
            f.write(f'{_k}={_v}\n')


def set_report_executer_on_results():
    """
    在allure-results报告的目录下生成一个写入了执行人的文件：executor.json
    @return:
    """
    # 需要写入的环境信息
    allure_executor = {
        "name": "张三",
        "type": "jenkins",
        "url": "www.baidu.com",  # allure报告的地址
        "buildOrder": 3,
        "buildName": "allure-report_deploy#1",
        "buildUrl": "www.baidu.com",
        "reportUrl": "www.baidu.com",
        "reportName": "张三 Allure Report"
    }
    xml_path = os.path.join(allure_xml_path, str(buildOrder))
    allure_env_file = os.path.join(xml_path, 'executor.json')
    with open(allure_env_file, 'w', encoding='utf-8') as f:
        f.write(str(json.dumps(allure_executor, ensure_ascii=False, indent=4)))


def get_dir():
    print("allure_path", allure_path)
    # 判断之前是否生成过报告
    first_path = "../allure_reports/allure_report/1"
    if os.path.exists(first_path):
        all_result_dir = os.listdir(allure_path)
        # 这个地方要注意，如果是mac，listdir获取到一个.DS_store的文件，使用下方的sort会报错，因而要先all_result_dir中将它remove掉
        all_result_dir.sort(key=int)

        # 取出最近一次执行的历史趋势的json
        history_file = os.path.join(allure_path, str(int(all_result_dir[-1])), 'widgets', 'history-trend.json')
        with open(history_file) as f:
            data = f.read()
        # 将下一次要生成的文件夹序号以及最新的历史趋势数据返回
        return int(all_result_dir[-1]) + 1, data
    else:
        # 如果之前没有生成过，就创建一个文件夹
        os.makedirs(os.path.join(allure_path, '1'))
        return 1, None


# 获取最新生成的趋势数据，这个数据里其实只有本次的结果，没有历史的结果
def update_new_single(buildOrder):
    new_single_file = os.path.join(allure_path, str(buildOrder), 'widgets', 'history-trend.json')
    with open(new_single_file, 'r+') as f:
        # data1 = f.read()
        data = json.load(f)
        # 写入本次是第几次执行、测试报告的路径
        data[0]["buildOrder"] = int(buildOrder)
        data[0]['reportUrl'] = f'http://localhost:63343/ttx_ofs_autoapi/allure_report/{str(buildOrder)}/index.html'
    with open(new_single_file, 'w+') as f:
        json.dump(data, f)


# 重写新生成的history-trend.json文件，用历史+本次=最新
def update_file(buildOrder):
    old_data = os.path.join(allure_path, str(int(buildOrder) - 1), 'widgets', 'history-trend.json')
    new_data = os.path.join(allure_path, str(int(buildOrder)), 'widgets', 'history-trend.json')
    with open(old_data) as f:
        old = json.load(f)
        dict = []
        for i in range(len(old)):
            dict.append(old[i])
        print(dict)
    with open(new_data) as f:
        r = f.read()
        new_list = ast.literal_eval(r)
        for i in range(len(dict)):
            new_list.append(dict[i])
    with open(new_data, 'w') as f:
        json.dump(new_list, f)


if __name__ == '__main__':
    print(allure_path)
    buildOrder, old_data = get_dir()
    # 先使用command生成xml文件
    xml_path = os.path.join(allure_xml_path, str(buildOrder))
    if not os.path.exists(xml_path):
        os.mkdir(xml_path)
    shutil.copy('../allure_reports/environment.xml', xml_path)
    shutil.copy('../allure_reports/categories.json', xml_path)

    # 在allure_results目录下创建environment.properties文件
    # set_report_env_on_results()

    # 在allure_results目录下创建executor.json文件
    set_report_executer_on_results()

    print(os.path.join(allure_xml_path, str(buildOrder)))
    command = f'pytest {test_path} -s --alluredir={os.path.join(allure_xml_path, str(buildOrder))}'
    os.system(command)

    # 再使用command1由xml生成json文件的测试报告
    # command1 = f'allure generate {os.path.join(allure_xml_path, str(buildOrder))} -o {os.path.join(allure_path, str(buildOrder))} --clean'
    command1 = f'allure generate {os.path.join(allure_xml_path, str(buildOrder))} -o {os.path.join(allure_path, str(buildOrder))} --clean'
    # command1 = f'allure generate {os.path.join(allure_xml_path, str(buildOrder))} -o {os.path.join(allure_path, str(buildOrder))} --clean-alluredir'
    print(command1)
    os.system(command1)
    update_new_single(buildOrder)
    if buildOrder != 1:
        update_file(buildOrder)

        # 在线报告
    os.system('allure serve  ' + os.path.join(allure_xml_path, str(buildOrder)))

    # ALLURE_DIR = os.path.dirname(__file__)
    # print(ALLURE_DIR)
    # ALLURE_PATH = os.path.join(ALLURE_DIR, str(int(time())))
    # # command = f'pytest {BASEDIR} -s --alluredir={ALLURE_PATH}'
    # # os.system(command)
    # # pytest.main(['-vs', '--alluredir=./result/tmp', __file__])
    # pytest.main(['-vs', '--alluredir=./result/tmp', '--clean-alluredir', __file__])
    #
    # # pytest.main(['-s', __file__])
    # shutil.copy('../allure_reports/environment.xml', './result/tmp')
    # shutil.copy('../allure_reports/categories.json', './result/tmp')
    # shutil.copy('../allure_reports/history-trend.json', './result/tmp')
    # pytest.main(['-vs', '--alluredir=./result/tmp', __file__])
    # # pytest.main(['-vs', '--alluredir=./result/tmp', '--clean-alluredir', __file__])
    #
    # # 离线报告
    # os.system('allure generate  ./result/tmp -o ./result/offline --clean')
    #
    # # 在线报告
    # os.system('allure serve  ./result/tmp')
