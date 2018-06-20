# -*- coding:utf-8 -*-  
'''
__author__:liubin 

'''
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import smtplib
import os
from conf import settings

def send_mail(report_file):

    with open(report_file, "rb") as f:
        mail_body = f.read()
    # 定义邮件内容
    msg = MIMEMultipart()
    body = MIMEText(mail_body, _subtype='html', _charset='utf-8')
    msg['Subject'] = u"接口测试报告"
    msg["from"] = settings.SENDER
    msg["to"] = settings.RECEIVER
    msg.attach(body)
    # 添加附件
    att = MIMEText(open(report_file, "rb").read(), "base64", "utf-8")
    att["Content-Type"] = "application/octet-stream"
    att["Content-Disposition"] = 'attachment; filename= "report.html"'
    msg.attach(att)
    try:
        smtp = smtplib.SMTP_SSL("smtp.qq.com", 465)
    except:
        smtp = smtplib.SMTP()
        smtp.connect("smtp.qq.com", 465)
    # 用户名密码
    smtp.login(settings.SENDER, settings.PWD)
    smtp.sendmail(settings.SENDER, settings.RECEIVER, msg.as_string())
    smtp.quit()



def get_report_file(report_path):
    '''第三步：获取最新的测试报告'''
    lists = os.listdir(report_path)
    lists.sort(key=lambda fn: os.path.getmtime(os.path.join(report_path, fn)))
    print (u'最新测试生成的报告： '+lists[-1])
    # 找到最新生成的报告文件
    report_file = os.path.join(report_path, lists[-1])
    return report_file