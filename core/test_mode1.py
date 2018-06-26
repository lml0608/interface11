# -*- coding:utf-8 -*-  
'''
__author__:liubin 

'''
import json
import requests
import unittest
from lib.log import Logger
from conf import settings


class TestStringMethods(unittest.TestCase):
    def setUp(self):
        self.logger = Logger()

        self.base_url = settings.HOST

    @unittest.skip('跳过')
    def test1(self):
        self.assertEqual(3, 5, msg='不相等')

    def test2(self):
        self.logger.log("nihao")
        self.assertEqual('hello', 'nihao')

    # 解码函数（装载）：将字符流转化为json对象
    # loads： 载入字符串变量
    # load：载入文件流
    # 编码函数（卸载）：将json对象转化为字符流
    # dumps：输出到字符串变量
    # dump：输出到文件流

    def test3(self):
        post_data = {
            "activityId": 0,
            "cusId": "686000660",
            "exchangeCode": "",
            "openId": "",
            "orderContext": {
                "proList": [
                    {
                        "code": "8",
                        "id": 8,
                        "name": "桃仁阿胶糕8",
                        "num": "2",
                        "price": 1,
                        "proImage": "string",
                        "skuName": "桃仁阿胶糕8",
                        "specialPrice": 0,
                        "templateId": "8",
                        "wareHouseCode": "555"
                    },
                    {
                        "code": "7",
                        "name": "百年老树鲜核桃7",
                        "num": "3",
                        "price": 2,
                        "proImage": "string",
                        "skuName": "2斤装",
                        "specialPrice": 0,
                        "templateId": "7",
                        "wareHouseCode": "888"
                    }
                ]
            },
            "phone": "string"
        }

        res = requests.post(url='sjd', data=post_data)

        res_dict = json.loads(res.text)

    def tearDown(self):
        pass

#
# def suite():
#
#     #装载测试用例
#     test_cases = unittest.TestLoader().loadTestsFromTestCase(TestStringMethods)
#
#     #使用测试套件并打包测试用例
#     test_suit = unittest.TestSuite()
#     test_suit.addTests(test_cases)
#
#     return test_suit


# if __name__ == '__main__':
#
#     #unittest.main()
#
#     #运行测试套件，并返回测试结果
#
#     test_result = unittest.TextTestRunner(verbosity=2).run(suite())
