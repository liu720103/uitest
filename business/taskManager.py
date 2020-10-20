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