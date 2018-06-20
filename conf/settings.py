# -*- coding:utf-8 -*-  
'''
__author__:liubin 

'''


import os


BASEDIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

TEST_PATH = os.path.join(BASEDIR,"core")
TEST_PATTERN = "test*.py"

ERROR_LOG_FILE = os.path.join(BASEDIR,"log",'error.log')

RUN_LOG_FILE = os.path.join(BASEDIR, "log", 'run.log')


HOST = 'test.wgmf.com'


#邮箱信息

SENDER = '183773928@qq.com'
PWD = 'ylqqhbgfohpfcahd'
RECEIVER = '343131230@qq.com'
SMTPSERVER = ''
PORT = ''


