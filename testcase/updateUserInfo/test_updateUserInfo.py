# -*- coding: utf-8 -*-
import sys
import time

from business import updatUserInfo
import allure
import testcase.updateUserInfo.conftest
import chardet
from flaky import flaky
reload(sys)
sys.setdefaultencoding('utf-8')

import pytest
#strs = "全国房屋建筑和市政设施风险普查系"
#print chardet.detect(strs)
#driver = conftest.driver()

@allure.step('1、进入修改用户信息界面')
def intoUpdateUserInfo(driver):
    updatUserInfo.login()
    return updatUserInfo.userInfo()

@allure.step('1、查看用户名用户账号')
def checkUserName(driver):
    return updatUserInfo.checkUserName()

@allure.step('1、不输入原密码修改用户姓名并点击提交')
def updateNameNopassword(driver, newName):
    return updatUserInfo.updateNameNopassword(content=newName)

@allure.step('1、输入原密码修改用户名并提交')
def updateName(driver, newname):
    return updatUserInfo.updateName(newname)

@allure.step('1、输入不符合格式的身份证号码')
def updateLegalUserID(driver, LegalUserID):
    updatUserInfo.updateUserID(LegalUserID)
    return updatUserInfo.getErrorMessage()

@allure.step('1、输入符合格式的身份证号码')
def updateRightUserID(driver, RightUserID):
    updatUserInfo.closeErrorMessage()
    updatUserInfo.updateUserID(RightUserID)
    return updatUserInfo.getUserID()

@allure.step('1、输入不符合格式联系电话')
def updateLegalPhoneNum(driver, LegalPhoneNum):
    updatUserInfo.updatePhoneNum(LegalPhoneNum)
    return updatUserInfo.getErrorMessage()

@allure.step('1、输入符合格式的联系电话')
def updateRightPhonNum(driver, RightPhoneNum):
    updatUserInfo.closeErrorMessage()
    updatUserInfo.updatePhoneNum(RightPhoneNum)
    return updatUserInfo.getPhoneNum()

@allure.step('1、输入新密码与确认密码不一致')
def differentPW(driver, pw1, pw2):
    updatUserInfo.updatePW(pw1,pw2)
    return updatUserInfo.getPWErrorMessage()

@allure.step('1、输入密码强度弱的密码')
def weakPW(driver, pw):
    updatUserInfo.updatePW(pw1=pw, pw2=pw)
    return updatUserInfo.getPWErrorMessage()

@allure.step('1、输入符合格式的密码')
def rightPW(driver, pw):
    updatUserInfo.updatePW(pw1=pw, pw2=pw)
    return updatUserInfo.loginPW(pw)

def login(driver):
    updatUserInfo.login()

def closeBrowser(dirver):
    updatUserInfo.closeBrowser()

@allure.feature('用户个人信息')
class TestupdateUserInfo():
    @classmethod
    def setUpClass(cls, driver):
        login(driver)

    @classmethod
    def tearDownClass(cls, driver):
        closeBrowser(driver)

    @allure.title('进入修改用户界面')
    def test_intoUpdateUserInfo(self, driver):
        assert intoUpdateUserInfo(driver) == u'修改用户信息'

    @allure.title('查看用户名用户账号')
    def test_checkUserName(self, driver):
        result = checkUserName(driver)
        assert result == u'110111105001'


    @allure.title('不输入原密码修改用户名')
    def test_updateNameNopassword(self, driver, newName = u'自动化测试工程师'):
        result = updateNameNopassword(driver, newName)
        assert result == u'需要输入原密码'


    @allure.title('输入原密码修改用户名')
    def test_updateName(self, driver):
        newName = u'自动化测试工程师'
        print newName
        result = updateName(driver, newName)
        assert result == newName

    @allure.title('输入不合法的身份证号码')
    def test_legalUserID(self, driver, LegalUserID = "11111"):
        result = updateLegalUserID(driver, LegalUserID)
        assert result == u'身份证号格式错误'

    @allure.title('输入合法身份证号')
    def test_updateRightUserID(self, driver, RightUserID = "430922199405193815"):
        result = updateRightUserID(driver, RightUserID)
        assert result == RightUserID

    @allure.title('输入不合法手机号码')
    def test_updateLegalPhoneNum(self, driver, legalPhoneNum="11111"):
        result = updateLegalPhoneNum(driver, legalPhoneNum)
        assert result == u'联系电话验证错误'

    @allure.title('输入合法手机号码')
    def test_updateRightPhoneNum(self, driver, rightPhoneNum="13059198197"):
        result = updateRightPhonNum(driver, rightPhoneNum)
        assert result == rightPhoneNum

    @allure.title('输入新密码与确认密码不一致')
    def test_differentPW(self, driver, pw1='aA123456', pw2='aA12345678'):
        assert differentPW(driver,pw1=pw1,pw2=pw2) == u'新密码与确认密码不一致'

    @allure.title('输入密码强度弱的密码')
    def test_weakPW(self, driver, pw='12345678'):
        assert weakPW(driver, pw) == u'新密码强度弱，重设新密码'

    @allure.title('输入符合格式的密码')
    def test_rightPW(self, driver, pw='aA123456'):
        assert rightPW(driver, pw) == u'全国房屋建筑和市政设施普查系统'
        closeBrowser(driver)