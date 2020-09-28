# -*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf8')
from readExcel import readExcel

def getPage(modulname, pagename):
    col1 = readExcel.read_excel(sheetname=modulname, col=1)
    col2 = readExcel.read_excel(sheetname=modulname, col=2)
    low = 0
    for i in col1:
        if i == pagename:
            break
        low = low+1
    return col2[low]

#getPage(modulname="login", pagename="密码")