# -*- coding:utf-8 -*-  
'''
__author__:liubin 

'''
import unittest
from conf import settings
from lib import send_email


def suite():


    test_cases = unittest.defaultTestLoader.\
        discover(settings.TEST_PATH,pattern=settings.TEST_PATTERN,top_level_dir=None)

    # #装载测试用例
    # test_cases = unittest.TestLoader().loadTestsFromTestCase(TestStringMethods)
    #
    # #使用测试套件并打包测试用例
    # test_suit = unittest.TestSuite()
    # test_suit.addTests(test_cases)

    return test_cases



if __name__ == '__main__':

    test_result = unittest.TextTestRunner(verbosity=2).run(suite())

    print(test_result.testsRun)
    send_email.send_mail('hello.html')

