# 对应的环境信息
import os, sys

BASE_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
REPORT_Path = os.path.join(BASE_PATH, 'report')
XML_path = os.path.join(REPORT_Path, 'xml')
HTML_path = os.path.join(REPORT_Path, 'html')
CASE_PATH = os.path.join(BASE_PATH, 'cases')
sys.path.insert(0, BASE_PATH)  # 把目录加入到环境变量里

#####邮箱信息
EMAIL_INFO = {
    'user': '',  # 发件箱
    'password': '',  # 邮箱授权码
    'to': [''],  # 收件邮箱
    'cc': [''],  ##抄送邮箱
    'subject': '测试环境接口自动化测试报告',  # 邮件标题
    'host': 'smtp.moqipobing.com',  ###邮件服务器
    'content': 'api自动化测试报告！，\nEnvironmental Science：测试环境 \n具体测试报告详情请下载附件查看，所有测试测试用例请点击ALL查看！',  # 邮件正文
    'attachments': ""
}
user = EMAIL_INFO.get('user')  # 从配置文件中获取邮件用户名
password = EMAIL_INFO.get('password')  # 从配置文件中获取邮件密码
to = EMAIL_INFO.get('to')  # 从配置文件中获取邮件接收者
cc = EMAIL_INFO.get('cc')  # 从配置文件中获取抄送者
subject = EMAIL_INFO.get('subject')  ##从配置文件中获取邮件标题
contents = EMAIL_INFO.get('content')  # 从配置文件中获取邮件内容
host = EMAIL_INFO.get('host')  ##从配置文件中获取邮箱服务器地址

##redis数控配置信息
REDIS_INFO = {
    'host': '',
    'port': ,
    'password': ''
}

####mysql数据库配置信息
MYSQL_INFO = {
    'host': '',
    'port': ,
    'user': '',
    'password': '',
    'db': 'main',
    'charset': 'utf8'
}
HOST_INFO = 'http://api.nnzhp.cn'
