# -*- coding: utf-8 -*-
import unittest
import sys
import allure
import os
import testcase.bridge.conftest
import chardet
reload(sys)
sys.setdefaultencoding('utf-8')
from business import bridge
import pytest
#strs = "全国房屋建筑和市政设施风险普查系"
#print chardet.detect(strs)
@allure.step('1、进入桥梁设施调查界面')
def intoBridge(driver):
    bridge.login()
    return bridge.intoBridge()
@allure.step('1、获取桥梁行政区划')
def getLocation(driver):
    return bridge.getlacation()

def login(driver):
    bridge.login()

def closeBrowser(dirver):
    bridge.closeBrowser()

@allure.feature('桥梁设施调查')
class TestupdateUserInfo():
    @classmethod
    def setUpClass(cls, driver):
        login(driver)

    @classmethod
    def tearDownClass(cls, driver):
        closeBrowser(driver)

    @allure.title('进入桥梁设施调查界面')
    def test_intoBridge(self, driver):
        assert intoBridge(driver) == u'桥梁设施调查'

    @allure.title('获取桥梁行政区划')
    def test_getLocation(self, driver):
        result = getLocation(driver)
        assert result[0] == u'北京市'
        #assert result[1] == u'市辖区'
        #assert result[2] == u'房山区'
        #assert result[3] == u'长阳镇'