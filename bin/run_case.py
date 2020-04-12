import unittest, time
from conf.setting import *
from lib.send_mail import *
from BeautifulReport import BeautifulReport
from lib.tools import get_newreport


def html_run():
    suite = unittest.TestSuite()  # 建立测试集合
    all_cases = unittest.defaultTestLoader.discover(CASE_PATH, '*.py')  # 把case目录下的所有测试用例.py加入到一个list里
    for case in all_cases:  # 循环测试用例list
        suite.addTests(case)  # 把测试用例.py加入到测试集合里
    run = BeautifulReport(suite)
    run.report(description='api自动化测试报告', filename="%s_report.html" % time.strftime('%Y%m%d%H%M%S'),
               report_dir=HTML_path)
    file_name = get_newreport()  # 获取新生成的测试报告
    send = Sendmail(user, password, host, to, cc, subject, contents, file_name)  # 实例化发邮件函数
    send.send_mail()  # 发送邮件


html_run()  # 运行程序，完成运行测试用例，校验结果，生成报告，发送邮件操作
