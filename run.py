# -*- coding: utf-8 -*-
from testcase import *
import pytest
import threading
import os

# 执行pytest单元测试，生成 Allure 报告需要的数据存在 /temp 目录
def runCase(testpy):
    pytest.main([testpy, '--alluredir', 'D:\\uitest\\temp'])
if __name__=="__main__":
    threads = []

    #testpys = ['testcase/login/test_login.py', 'testcase/userManager/test_userManager.py', 'testcase/updateUserInfo/test_updateUserInfo.py']
    testpys = ['testcase/bridge/test_bridge.py']
    for i in testpys:
        t = threading.Thread(target=runCase(i))
        threads.append(t)

    file = range(len(testpys))
    for i in file:
        threads[i].start()
    for i in file:
        threads[i].join()

os.system('allure generate D:\\uitest\\temp -o D:\\uitest\\report --clean')

'''
pytest.main(['testcase/test_login.py', '--alluredir', 'D:\\uitest\\temp'])
pytest.main(['testcase/test_userManager.py', '--alluredir', 'D:\\uitest\\temp'])
# 执行命令 allure generate ./temp -o ./report --clean ，生成测试报告
os.system('allure generate D:\\uitest\\temp -o D:\\uitest\\report --clean')

# 执行pytest单元测试，生成 Allure 报告需要的数据存在 /temp 目录
pytest.main(['--alluredir', 'C:\\Users\\11458\\.jenkins\\workspace\\zaihaipucha\\target\\allure-results'])
# 执行命令 allure generate ./temp -o ./report --clean ，生成测试报告
os.system('allure generate C:\\Users\\11458\\.jenkins\\workspace\\zaihaipucha\\target\\allure-results -o D:\\uitest\\report --clean')
'''
