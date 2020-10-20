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
