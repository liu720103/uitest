# -*- coding: utf-8 -*-
import unittest
import sys
import allure
import os
import testcase.userManager.conftest
import chardet
reload(sys)
sys.setdefaultencoding('utf-8')
from business import loginBusiness
import pytest
#strs = "全国房屋建筑和市政设施风险普查系"
#print chardet.detect(strs)
@allure.step('1、查看APP二维码下载')
def APPImg(driver):
    return loginBusiness.clickAPP()

@allure.step('1、输入正确账号错误密码点击登录')
def loginErrorPassword(driver):
    return loginBusiness.loginError(username='fstest3', password='12345678')

@allure.step('1、输入空账号点击登录')
def loginUsernameEmpty(driver):
    return loginBusiness.loginUsernameEmpty(username='', password='123456')

@allure.step('1、输入空密码点击登录')
def loginPasswordEmpty(driver):
    return loginBusiness.loginPassworEmpty(username='fstest3', password='')

@allure.step('1、输入正确账号正确密码')
def login(driver):
    result = loginBusiness.login(username='fstest3', password='aA123456')
    return result

def closeBrower(driver):
    loginBusiness.closeBrowser()

@allure.feature('登录模块')
class Testlogin():

    @classmethod
    def tearDownClass(cls, driver):
        closeBrower(driver)

    @allure.title('查看APP二维码下载')
    def test_APPImg(self, driver):
        assert u"扫描二维码直接下载安装" == APPImg(driver)

    #@pytest.mark.run(order=2)
    @allure.title('输入正确账号错误密码')
    def test_loginErrorPassword(self, driver):
        assert u"账号或者密码错误" == loginErrorPassword(driver)

    #@pytest.mark.run(order=3)
    @allure.title('输入空用户')
    def test_loginUsernameEmpty(self, driver):
        assert u"请输入用户名" == loginUsernameEmpty(driver)

    #@pytest.mark.run(order=4)
    @allure.title('输入空密码')
    def test_loginPasswordEmpty(self, driver):
        assert u"请输入密码" == loginPasswordEmpty(driver)


    @allure.title('输入正确账号正确密码')
    def test_login(self, driver):
        assert u"全国房屋建筑和市政设施普查系统" == login(driver)
        closeBrower(driver)


