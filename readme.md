﻿框架说明：
本框架可实现接口的自动化测试
流程：自动化测试用例编写=》自动化执行测试用例=》生成报告=》发送邮件
框架目录：
bin目录：总入口目录，程序执行入口目录
cases目录：自动化测试用例存放目录
conf目录：配置文件目录
lib目录：逻辑目录（功能目录）
report目录：测试报告存放目录

注：BeautifulReport.py文件为测试报告模板文件，case基于这个文件而运行后生产测试报告，BeautifulReport目录必须放于python的安装目录下的Lib\site-packages目录下
