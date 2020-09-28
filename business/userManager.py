# -*- coding: utf-8 -*-
import logging
import time

from testcase.userManager import conftest
from page.getPage import getPage
#conftest.driver()
#开启浏览器

def get_page(pagename):
    return getPage(modulname='usermanager', pagename=pagename)

def get_loginpage(pagename):
    return getPage(modulname='login', pagename=pagename)

#进入用户管理界面
def intoUserManager():
    conftest.click(ele=get_page('系统管理'))
    conftest.click(ele=get_page('用户管理'))
    return conftest.getText(ele=get_page('新增用户'))

#点击新增用户
def clickAddUser():
    time.sleep(3)
    return conftest.click(ele=get_page('新增用户'))


#点击查询用户
def clickSelectUser(content):
    conftest.send_keys(ele=get_page('查询框'),content=content)
    conftest.click(ele=get_page('查询'))

#获取未选择机构时新增用户页面提示信息
def AdduserNoDepart():
    if clickAddUser() == True:
        print "新增用户按钮点击成功"
        return conftest.getText(ele=get_page('无机构新增用户提示'))
    else:
        return "新增用户按钮点击失败"

#获取未选择机构时查询用户页面提示信息
def selectUserNoDepart(content):
    time.sleep(3)
    clickSelectUser(content)
    return conftest.getText(ele=get_page('无机构查询用户提示'))
#点击房山区
def clickFangshan():
    conftest.click(ele=get_page('房山区'))

#选择机构点击新增
def addUserHaveDepart(ManagerNum,InvestigatorNum,isSubmit=None,password=None,Isxiangzhen=None,passwordType=None):
    clickFangshan()
    clickAddUser()
    conftest.send_keys(ele=get_page('各级管理员数量'),content=ManagerNum)
    conftest.send_keys(ele=get_page('各级调查员数量'),content=InvestigatorNum)
    if Isxiangzhen == 'yes':
        conftest.click(ele=get_page('创建子机构用户'))
    if passwordType == '相同':
        conftest.click(ele=get_page('相同密码'))
        conftest.send_keys(ele=get_page('相同密码输入'), content=password)
    if isSubmit == 'no':
        conftest.click(ele=get_page('取消'))
    else:
        conftest.click(ele=get_page('提交'))
#取消新增用户
def noAddUser():
    conftest.click(ele=get_page('取消'))

#新增用户不合法输入提示
def getLegalMessage():
    return conftest.getText(ele=get_page('不合法提示'))

#成功新增用户提示
def getRightMessage():
    return conftest.getText(ele=get_page('完成新增用户提示'))

#点击重置按钮
def clickReset():
    conftest.click(ele=get_page('重置'))

#获取表格用户名
def tableUsername():
    return conftest.getText(ele=get_page('用户名'))

#获取表格姓名
def tableName():
    return conftest.getText(ele=get_page('姓名'))

#获取表格联系电话
def tableTel():
    return conftest.getText(ele=get_page('联系电话'))

#获取表格所属机构
def tableDepartment():
    return conftest.getText(ele=get_page('所属机构'))

#获取表格是否启用
def tableIsUse():
    return conftest.getText(ele=get_page('是否启用'))

#获取表格操作
def tableDo():
    return conftest.click(ele=get_page('操作'))

#修改用户姓名
def updateName(newName):
    tableDo()
    conftest.send_keys(ele=get_page('修改姓名'),content=newName)
    conftest.click(ele=get_page('修改提交'))

#修改用户身份证号码
def updateUserID(userID):
    time.sleep(1)
    tableDo()
    conftest.send_keys(ele=get_page('修改身份证号码'),content=userID)
    conftest.click(ele=get_page('修改提交'))

#获取身份证号错误提示信息
def getLegalUserIDMessage():
    return conftest.getText(ele=get_page('身份证错误提示'))

#获取用户身份证号码
def getUserID():
    tableDo()
    return conftest.getInputText(ele=get_page('修改身份证号码'))


#修改用户联系电话
def upadateUserTel(Tel):
    tableDo()
    conftest.send_keys(ele=get_page('修改联系电话'),content=Tel)
    conftest.click(ele=get_page('修改提交'))

#获取联系电话错误提示信息
def getLegalTelMessage():
    return conftest.getText(ele=get_page('联系电话错误提示'))

#获取用户手机号码
def getTel():
    tableDo()
    return conftest.getInputText(ele=get_page('修改联系电话'))

#修改用户是否启用
def updateIsUse(IsUse):
    tableDo()
    conftest.click(ele=get_page('修改是否启用'))
    if IsUse == 'yes':
        conftest.click(ele=get_page('修改启用'))
    else:
        conftest.click(ele=get_page('修改禁用'))
    conftest.click(ele=get_page('修改提交'))

#用户登录
def loginDo(username, password):
    conftest.send_keys(ele=get_loginpage('账号'), content=username)
    conftest.send_keys(ele=get_loginpage('密码'), content=password)
    conftest.click(ele=get_loginpage('登录'))

#禁用用户登录用户不存在提示
def noUserMessage():
    return conftest.getText(ele=get_loginpage('提示'))

#用户登录获取成功提示
def userLoginMessage():
    return conftest.getText(ele=get_loginpage('标题'))

#修改用户密码
def updatePassword(newPassword):
    tableDo()
    conftest.send_keys(ele=get_page('修改密码'),content=newPassword)
    conftest.click(ele=get_page('修改提交'))

#获取用户名
def getUserName():
    tableDo()
    username = conftest.getInputText(ele=get_page('修改用户名'))
    noUpdateUserMessage()
    return username

#取消修改用户信息
def noUpdateUserMessage():
    conftest.click(ele=get_page('修改取消'))

#用户登出系统
def logout():
    conftest.click(ele=get_page('登出'))

#关闭浏览器
def closeBrowser():
    conftest.closeBrowser()