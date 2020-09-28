# -*- coding: utf-8 -*-
import logging
from testcase.login import conftest
from page.getPage import getPage
#conftest.driver()

def get_page(pagename):
    return getPage(modulname='login', pagename=pagename)

#点击APP应用
def clickAPP():
    conftest.click(ele=get_page('APP应用'))
    result = conftest.getText(ele=get_page('APP提示语'))
    conftest.click(ele=get_page('密码登录'))
    return result

#登录操作
def loginDo(username, password):
    conftest.send_keys(ele=get_page('账号'), content=username)
    conftest.send_keys(ele=get_page('密码'), content=password)
    conftest.click(ele=get_page('登录'))

#空账号
def loginUsernameEmpty(username, password):
    loginDo(username, password)
    return conftest.getText(ele=get_page('空用户'))

#空密码
def loginPassworEmpty(username, password):
    loginDo(username, password)
    return conftest.getText(ele=get_page('空密码'))

#正确账号错误密码
def loginError(username, password):
    loginDo(username, password)
    return conftest.getText(ele=get_page('提示'))

#正确账号正确密码
def login(username, password):
    loginDo(username, password)
    return conftest.getText(ele=get_page('标题'))

#关闭浏览器操作
def closeBrowser():
    conftest.closeBrowser()


