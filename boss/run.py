import HTMLTestRunner
from pages.testsuit.testlogin import *
import unittest
import os

# 设置报告文件保存路径
report_path = os.path.dirname(os.path.abspath('.')) + '/boss/logs/report/'
# 获取系统当前时间
now = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
# 设置报告名称格式
filename = report_path + now + "HTMLtemplate.html"
fp = open(filename, "wb")
if __name__ == '__main__':
    #构造测试集
    suite = unittest.TestSuite()
    suite.addTest(TestLogin("test_login_success"))
    runner = unittest.TextTestRunner()
    #runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title=u"Fii富集运商城项目测试报告", description=u"用例测试情况",tester=u"段治维")
    runner.run(suite)

