# -*- coding: utf-8 -*-
import logging
import time

from testcase.bridge import conftest
from page.getPage import getPage
#conftest.driver()
#开启浏览器
def get_page(pagename):
    return getPage(modulname='bridge', pagename=pagename)

def get_loginpage(pagename):
    return getPage(modulname='login', pagename=pagename)

#登录灾害普查系统
def login():
    conftest.send_keys(ele=get_loginpage('账号'), content=u'110111105001')
    conftest.send_keys(ele=get_loginpage('密码'), content='aA123456')
    conftest.click(ele=get_loginpage('登录'))

#关闭浏览器
def closeBrowser():
    conftest.closeBrowser()

#进入桥梁设施调查界面
def intoBridge():
    conftest.click(ele=get_page('任务管理'))
    conftest.click(ele=get_page('我的任务'))
    conftest.click(ele=get_page('桥梁调查'))
    time.sleep(1)
    conftest.click(ele=get_page('查询'))
    conftest.send_keys(ele=get_page('任务名称'), content=u'长阳镇(自动化测试工程师专用任务切勿删除)')
    conftest.click(ele=get_page('查询按钮'))
    time.sleep(2)
    conftest.click(ele=get_page('桥梁调查按钮'))
    time.sleep(1)
    return conftest.getText(ele=get_page('桥梁设施调查'))

#获取桥梁行政区划
def getlacation():
    conftest.click(ele=get_page('调查'))
    location = []
    location.append(conftest.getText(ele=get_page('北京市')))
    #location.append(conftest.getText(ele=get_page('市辖区')))
    #location.append(conftest.getText(ele=get_page('房山区')))
    #location.append(conftest.getText(ele=get_page('长阳镇')))
    return location