# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from readExcel import readExcel
import time
import os
import pytest
import allure

"驱动浏览器"
@pytest.fixture(scope='session', autouse=True)
def driver():
    global driver
    config = readExcel.read_excel(sheetname="config",col=2)
    exepath = config[0]
    url = config[1]
    driver = webdriver.Chrome(exepath)
    driver.maximize_window()
    driver.get(url)
    return driver
"等待至元素可见"
def visiElement(ele):
    try:
        ele = ele.split('>>')
        # print ele[0]
        if ele[0] == "class":
            result = WebDriverWait(driver, 30, 0.5).until(EC.visibility_of_element_located((By.CLASS_NAME, ele[1])))
        if ele[0] == "id":
            result = WebDriverWait(driver, 30, 0.5).until(EC.visibility_of_element_located((By.ID, ele[1])))
        if ele[0] == "xpath":
            result = WebDriverWait(driver, 30, 0.5).until(EC.visibility_of_element_located((By.XPATH, ele[1])))
        return result
    except:
        print('%s页面未找到元素' % ele)

"寻找元素"
def find_element(ele):
    try:
        ele = ele.split('>>')
        #print ele[0]
        if ele[0] == "id":
            #WebDriverWait(driver, 60).until(EC.visibility_of_element_located((By.ID, ele[1])))
            #WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.ID, ele[1])))  # 显示等待
            result = WebDriverWait(driver, 30, 0.5).until(EC.element_to_be_clickable((By.ID,ele[1])))
            #result = driver.find_element_by_id(ele[1])
        if ele[0] == "xpath":
            #WebDriverWait(driver, 60).until(EC.visibility_of_element_located((By.XPATH, ele[1])))
            #WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.XPATH, ele[1])))
            result = WebDriverWait(driver, 30, 0.5).until(EC.element_to_be_clickable((By.XPATH, ele[1])))
            #result = driver.find_element_by_xpath(ele[1])
        if ele[0] == "class":
            #WebDriverWait(driver, 60).until(EC.visibility_of_element_located((By.CLASS_NAME, ele[1])))
            #WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.CLASS_NAME, ele[1])))
            result = WebDriverWait(driver, 30, 0.5).until(EC.element_to_be_clickable((By.CLASS_NAME, ele[1])))
            #driver.find_element_by_class_name(ele[1])
        return result
    except:
        print('%s页面未找到元素'% ele)

"输入框输入内容"
def send_keys(ele, content):
    find_element(ele).clear()
    find_element(ele).send_keys(content)

"单击按钮"
def click(ele):
    try:
        find_element(ele).click()
        return True
    except:
        return False

"获取标签内容"
def getText(ele):
    try:
        content = visiElement(ele).text
        return content
    except:
        print "未找到"+ele
        return None

"获取输入框中的值"
def getInputText(ele):
    try:
        content = visiElement(ele).get_attribute('value')
        return content
    except:
        return "未找到"+ele

"失败错误截图"
def screen_image():
    """
        对当前页面进行截图
        :return:
        """
    start_time = time.time()
    filename = '{}.png'.format(start_time)
    file_path = os.path.join("D:\\uitest\\errorImg", filename)
    driver.save_screenshot(file_path)
    return file_path

"保存错误截图"
def save_image_to_allure():
    """
    保存失败的截图到allure报告中
    :return:
    """
    file_path = screen_image()
    with open(file_path, "rb") as f:
        file = f.read()
        allure.attach(file, "失败截图", allure.attachment_type.PNG)

@pytest.mark.hookwrapper
def pytest_runtest_makereport(item):
    """
    Extends the PyTest Plugin to take and embed screenshot in html report, whenever test fails.
    :param item:
    """
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])

    if report.when == 'call' or report.when == "setup":
        xfail = hasattr(report, 'wasxfail')
        #判断用例是否失败或者xfail跳过的测试
        if (report.skipped and xfail) or (report.failed and not xfail):
        	#获取测试用例代码中webDriver参数来获取浏览器进行抓屏
            for i in item.funcargs:
                if isinstance(item.funcargs[i], WebDriver):
                	#截图
                    save_image_to_allure()
                    pass
                pass
            pass
        report.extra = extra
"关闭浏览器"
def closeBrowser():
    driver.quit()

#driver()
#send_keys(ele="username",content="fstest3")

#print ("你好")