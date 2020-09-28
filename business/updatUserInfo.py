# -*- coding: utf-8 -*-
import logging
import time

from testcase.updateUserInfo import conftest
from page.getPage import getPage
#conftest.driver()
#开启浏览器

def get_page(pagename):
    return getPage(modulname='updateuserinfo', pagename=pagename)

def get_loginpage(pagename):
    return getPage(modulname='login', pagename=pagename)

#登录灾害普查系统
def login():
    conftest.send_keys(ele=get_loginpage('账号'), content=u'110111105001')
    conftest.send_keys(ele=get_loginpage('密码'), content='aA123456')
    conftest.click(ele=get_loginpage('登录'))

#密码登录
def loginPW(PW):
    conftest.click(ele=get_page('登出'))
    conftest.send_keys(ele=get_loginpage('账号'), content=u'110111105001')
    conftest.send_keys(ele=get_loginpage('密码'), content=PW)
    conftest.click(ele=get_loginpage('登录'))
    time.sleep(3)
    return conftest.getText(ele=get_loginpage('标题'))

#关闭浏览器
def closeBrowser():
    conftest.closeBrowser()

#点击用户个人信息加载修改用户信息界面
def userInfo():
    b = '未找到xpath>>//*[@id="layui-layer1"]/div[1]'
    while b == '未找到xpath>>//*[@id="layui-layer1"]/div[1]':
        conftest.click(ele=get_page('用户信息'))
        b = conftest.getText(ele=get_page('修改用户信息'))
    return b

#查看用户账号
def checkUserName():
    num = 1
    result = None
    while num < 10:
        num = num+1
        result = conftest.getInputText(ele=get_page('用户名'))
    return result

#修改用户姓名信息不输入原密码
def updateNameNopassword(content):
    conftest.send_keys(ele=get_page('姓名'), content=content)
    conftest.click(ele=get_page('提交'))
    return conftest.getText(ele=get_page('无原密码提示'))

#修改用户名信息
def updateName(content):
    conftest.click(ele=get_page('取消'))
    conftest.click(ele=get_page('用户信息'))
    time.sleep(2)
    conftest.send_keys(ele=get_page('姓名'),content=content)
    conftest.send_keys(ele=get_page('原密码'),content=u'aA123456')
    conftest.click(ele=get_page('提交'))
    conftest.click(ele=get_page('用户信息'))
    time.sleep(2)
    return conftest.getInputText(ele=get_page('姓名'))

#获取用户身份证号码
def getUserID():
    conftest.click(ele=get_page('用户信息'))
    a = 1
    result = None
    while a < 10:
        a = a+1
        result = conftest.getInputText(ele=get_page('身份证号码'))
    return result

#修改用户身份证号码
def updateUserID(userID):
    conftest.send_keys(ele=get_page('身份证号码'), content=userID)
    conftest.send_keys(ele=get_page('原密码'), content=u'aA123456')
    conftest.click(ele=get_page('提交'))

#获取用户手机号码
def getPhoneNum():
    conftest.click(ele=get_page('用户信息'))
    a = 1
    result = None
    while a < 10:
        a = a+1
        result = conftest.getInputText(ele=get_page('联系电话'))
    return result

#修改用户手机号码
def updatePhoneNum(PhoneNum):
    conftest.send_keys(ele=get_page('联系电话'), content=PhoneNum)
    conftest.send_keys(ele=get_page('原密码'), content=u'aA123456')
    conftest.click(ele=get_page('提交'))

#获取身份证或手机号码错误提示
def getErrorMessage():
    return conftest.getText(ele=get_page('错误提示'))

#关闭身份证或手机号码错误提示
def closeErrorMessage():
    return conftest.click(ele=get_page('关闭错误提示'))

#输入密码
def updatePW(pw1,pw2):
    conftest.send_keys(ele=get_page('新密码'), content=pw1)
    conftest.send_keys(ele=get_page('确认新密码'), content=pw2)
    conftest.send_keys(ele=get_page('原密码'), content=u'aA123456')
    conftest.click(ele=get_page('提交'))

#获取密码提示
def getPWErrorMessage():
    return conftest.getText(ele=get_page('密码提示'))