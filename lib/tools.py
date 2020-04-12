from conf.setting import REPORT_Path
from hashlib import md5
import os


def myMd5(st):
    SECRET_KEY = '68@63fc1jkyu4m+wlvyc5(0gik12u9o90tm5q^l^_w^9^%7=zl'
    st = str(st)
    md = md5()
    st = SECRET_KEY + st
    md.update(st.encode())
    return md.hexdigest()


####清除测试报告目录文件
def remove_report():
    html_path = os.path.join(REPORT_Path, 'html')
    all_report = os.listdir(html_path)
    for list in all_report:
        abs_path = os.path.join(html_path, list)
        os.remove(abs_path)


def get_newreport():
    html_path = os.path.join(REPORT_Path, 'html')
    all_report = os.listdir(html_path)
    file_name = all_report[-1]
    abs_path = os.path.join(html_path, file_name)
    return abs_path
