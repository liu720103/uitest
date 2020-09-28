# -*- coding: utf-8 -*-
import sys
import allure
import os
import time
import pytest_ordering
import testcase.userManager.conftest
import chardet
from flaky import flaky
reload(sys)
sys.setdefaultencoding('utf-8')
from business import userManager
import pytest
#strs = "全国房屋建筑和市政设施风险普查系"
#print chardet.detect(strs)
#driver = conftest.driver()
@allure.step('1、进入用户管理界面')
def intoUserManager(driver):
    userManager.loginDo(username='fstest3', password='aA123456')
    return userManager.intoUserManager()

@allure.step('1、未选择机构点击新增用户')
def addUserNoDepart(dirver):
    return userManager.AdduserNoDepart()

@allure.step('1、未选择机构点击查询用户')
def selectUserNoDepart(driver):
    return userManager.selectUserNoDepart(content="123")

@allure.step('1、各级管理员数量输入负数')
def legalManagerNum(driver):
    userManager.addUserHaveDepart(ManagerNum=-1,InvestigatorNum=0)
    result = userManager.getLegalMessage()
    userManager.noAddUser()
    return result

@allure.step('1、各级管理员数量输入正数')
def rightManagerNum(driver):
    userManager.addUserHaveDepart(ManagerNum=1,InvestigatorNum=0)
    return userManager.getRightMessage()

@allure.step('1、调查员数量输入负数')
def legalInvestigatorNum(driver):
    userManager.addUserHaveDepart(ManagerNum=0,InvestigatorNum=-1)
    result = userManager.getLegalMessage()
    userManager.noAddUser()
    return result

@allure.step('1、调查员数量输入正数')
def rightInvestigatorNum(driver):
    userManager.addUserHaveDepart(ManagerNum=0, InvestigatorNum=1)
    return userManager.getRightMessage()

@allure.step('1、根据用户名查询用户')
def selectUserByUsername(driver):
    userManager.clickSelectUser(content='110111105001')
    time.sleep(3)
    result = userManager.tableUsername()
    userManager.clickReset()
    return result

@allure.step('1、根据用户姓名查询用户')
def selectByName(driver):
    userManager.clickSelectUser(content=u'自动化测试工程师')
    time.sleep(3)
    result = userManager.tableName()
    return result

@allure.step('1、根据联系电话查询用户')
def selectByTel(driver):
    userManager.clickSelectUser(content='13059198197')
    time.sleep(3)
    result = userManager.tableTel()
    userManager.clickReset()
    return result
@allure.step('1、修改用户姓名')
def updateName(driver):
    newName = u'自动化测试'
    oldName = u'自动化测试工程师'
    userManager.updateName(newName)
    time.sleep(2)
    userManager.clickSelectUser(newName)
    result = userManager.tableName()
    userManager.updateName(oldName)
    return result

@allure.step('1、输入不合法身份证号码')
def legalUserID(driver,legalUserID):
    time.sleep(2)
    userManager.updateUserID(userID=legalUserID)
    result = userManager.getLegalUserIDMessage()
    userManager.noUpdateUserMessage()
    return result

@allure.step('1、输入合法身份证号码')
def rightUserID(driver,rightUserID):
    userManager.updateUserID(userID=rightUserID)
    time.sleep(2)
    return userManager.getUserID()

@allure.step('1、输入不合法手机号码')
def legalTel(driver, legalTel):
    userManager.noUpdateUserMessage()
    userManager.upadateUserTel(Tel=legalTel)
    result = userManager.getLegalTelMessage()
    return result

@allure.step('1、输入合法手机号码')
def rightTel(driver, rightTel):
    userManager.noUpdateUserMessage()
    userManager.upadateUserTel(Tel=rightTel)
    time.sleep(1)
    return userManager.getTel()

@allure.step('1、禁用账户使用禁用账户登录')
def noUseUser(driver):
    userManager.noUpdateUserMessage()
    userManager.updateIsUse(IsUse='no')
    username = userManager.getUserName()
    userManager.logout()
    userManager.loginDo(username=username, password='aA123456')
    return userManager.noUserMessage()

@allure.step('1、启用账户使用启用账户登录')
def isUseUser(driver):
    userManager.loginDo(username='fstest3', password='aA123456')
    userManager.intoUserManager()
    userManager.clickFangshan()
    userManager.clickSelectUser(u'自动化测试工程师')
    time.sleep(3)
    userManager.updateIsUse(IsUse='yes')
    username = userManager.getUserName()
    userManager.logout()
    userManager.loginDo(username=username, password='aA123456')
    result = userManager.userLoginMessage()
    time.sleep(5)
    userManager.logout()
    return result

@allure.step('1、输入密码使用新密码登录')
def updatePassword(driver, newpassword):
    time.sleep(5)
    userManager.loginDo(username='fstest3', password='aA123456')
    userManager.intoUserManager()
    userManager.clickFangshan()
    userManager.clickSelectUser(u'自动化测试工程师')
    time.sleep(3)
    userManager.updatePassword(newPassword=newpassword)
    username = userManager.getUserName()
    userManager.logout()
    userManager.loginDo(username=username,password=newpassword)
    result = userManager.userLoginMessage()
    return result

def closeBrowser(dirver):
    userManager.closeBrowser()

@allure.feature('用户管理模块')
class TestuserManager():

    @classmethod
    def tearDownClass(cls, driver):
        closeBrowser(driver)

    @allure.title('进入用户管理')
    def test_intoUserManager(self, driver):
        result = intoUserManager(driver)
        assert result == u'新增用户'

    @allure.title('未选择机构点击新增用户')
    def test_addUserNodepart(self, driver):
        assert addUserNoDepart(driver) == u'请先选取机构，再新增'

    @allure.title('未选择机构点击查询')
    def test_selectUserNodepart(self, driver):
        assert selectUserNoDepart(driver) == u'请先选取机构，再查询'

    @allure.title('新增用户管理员数量输入负数')
    def test_legalManagerNum(self, driver):
        assert legalManagerNum(driver) == u'* 最小值为 0'

    @allure.title('新增用户管理员数量输入正数')
    def test_rightManagerNum(self, driver):
        assert rightManagerNum(driver) == u'创建用户成功'

    @allure.title('新增用户调查员数量输入负数')
    def test_legalInvestigatorNum(self, driver):
        assert legalInvestigatorNum(driver) == u'* 最小值为 0'

    @allure.title('新增用户调查员数量输入正数')
    def test_rightInvestigatouNum(self, driver):
        assert rightInvestigatorNum(driver) == u'创建用户成功'

    @allure.title('根据用户名查询用户')
    def test_selectByUsername(self, driver):
        assert selectUserByUsername(driver) == u'110111105001'

    @allure.title('根据电话号码查询用户')
    def test_selectByTel(self, driver):
        assert selectByTel(driver) == u'13059198197'

    @allure.title('根据姓名查询用户')
    def test_selectByName(self, driver):
        assert selectByName(driver) == u'自动化测试工程师'

    @allure.title('修改用户姓名')
    def test_updateName(self, driver):
        assert updateName(driver) == u'自动化测试'

    @allure.title('输入不合法身份证号码')
    def test_legalUserID(self, driver):
        assert legalUserID(driver=driver, legalUserID=u'1111') == u'身份证号格式错误'

    @allure.title('输入合法身份证号码')
    def test_rightUserID(self, driver):
        assert rightUserID(driver=driver, rightUserID=u'430922199405193815') == u'430922199405193815'

    @allure.title('输入不合法联系电话')
    def test_legalTel(self, driver):
        assert legalTel(driver=driver, legalTel='1111') == u'联系电话验证错误'

    @allure.title('输入合法联系电话')
    def test_rightTel(self, driver):
        assert rightTel(driver=driver, rightTel='13059198197') == '13059198197'

    @allure.title('使用禁用账户登录')
    def test_noUseUser(self, driver):
        assert noUseUser(driver=driver) == u'用户不存在'

    @allure.title('使用启用账户登录')
    def test_isUseUser(self, driver):
        assert isUseUser(driver) == u'全国房屋建筑和市政设施风险普查系统'

    @allure.title('修改用户密码')
    #@flaky(max_runs=3, min_passes=2)
    def test_updatePassword(self, driver):
        assert updatePassword(driver=driver, newpassword='aA123456') == u'全国房屋建筑和市政设施风险普查系统'

