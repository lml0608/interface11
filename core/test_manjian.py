# -*- coding:utf-8 -*-  
'''
__author__:liubin 

'''

import json
import requests
import unittest
from lib.log import Logger
from conf import settings
import json
import operator


class TestManjian(unittest.TestCase):

    """
    设置满减活动没有产品和组合，只有订单金额，梯度满减
    """
    def setUp(self):
        self.url = 'http://test.wgmf.com/promotion-online/online/validActivity'

    def test_get_activity(self):

        # 满10减5

        post_data = {
            "activityId": 0,
            "cusId": "16788112",
            "exchangeCode": "",
            "openId": "",
            "orderContext": {
                "proList": [
                    {
                        "code": "9",
                        "name": "中宁枸杞初心蜜",
                        "num": "3",
                        "price": 5,
                        "proImage": "string",
                        "skuName": "规格",
                        "specialPrice": 0,
                        "templateId": "9",
                        "wareHouseCode": "666"
                    }
                ]
            },
            "phone": "string"
        }

        res = requests.post(url=self.url, json=post_data)

        res_dict = json.loads(res.text)

        activityId = res_dict['resultInfo'][0]['activityInfo']['activityId']
        giftmoney = res_dict['resultInfo'][0]['giftRuleResultContext']['giftMoney']

        self.assertEqual(activityId,6447, msg="结果不匹配")
        self.assertEqual(giftmoney,5,msg="减少金额应该是5")


        # 订单金额小于10

        post_data = {
            "activityId": 0,
            "cusId": "16788112",
            "exchangeCode": "",
            "openId": "",
            "orderContext": {
                "proList": [
                    {
                        "code": "9",
                        "name": "中宁枸杞初心蜜",
                        "num": "3",
                        "price": 3,
                        "proImage": "string",
                        "skuName": "规格",
                        "specialPrice": 0,
                        "templateId": "9",
                        "wareHouseCode": "666"
                    }
                ]
            },
            "phone": "string"
        }

        res = requests.post(url=self.url, json=post_data)

        res_dict = json.loads(res.text)

        activity_list = res_dict['resultInfo']

        self.assertEqual(len(activity_list),0,msg="活动信息列表应该为空")

        # 满20减10  梯度满减

        post_data = {
            "activityId": 0,
            "cusId": "16788112",
            "exchangeCode": "",
            "openId": "",
            "orderContext": {
                "proList": [
                    {
                        "code": "9",
                        "name": "中宁枸杞初心蜜",
                        "num": "2",
                        "price": 10,
                        "proImage": "string",
                        "skuName": "规格",
                        "specialPrice": 0,
                        "templateId": "9",
                        "wareHouseCode": "666"
                    }
                ]
            },
            "phone": "string"
        }

        res = requests.post(url=self.url, json=post_data)

        res_dict = json.loads(res.text)

        activityId = res_dict['resultInfo'][0]['activityInfo']['activityId']
        giftmoney = res_dict['resultInfo'][0]['giftRuleResultContext']['giftMoney']

        self.assertEqual(activityId,6447, msg="结果不匹配")
        self.assertEqual(giftmoney,10,msg="减少金额应该是10")



        # 满30减15  梯度满减

        post_data = {
            "activityId": 0,
            "cusId": "16788112",
            "exchangeCode": "",
            "openId": "",
            "orderContext": {
                "proList": [
                    {
                        "code": "9",
                        "name": "中宁枸杞初心蜜",
                        "num": "3",
                        "price": 10,
                        "proImage": "string",
                        "skuName": "规格",
                        "specialPrice": 0,
                        "templateId": "9",
                        "wareHouseCode": "666"
                    }
                ]
            },
            "phone": "string"
        }

        res = requests.post(url=self.url, json=post_data)

        res_dict = json.loads(res.text)

        activityId = res_dict['resultInfo'][0]['activityInfo']['activityId']
        giftmoney = res_dict['resultInfo'][0]['giftRuleResultContext']['giftMoney']

        self.assertEqual(activityId,6447, msg="结果不匹配")
        self.assertEqual(giftmoney,15,msg="减少金额应该是10")
    def tearDown(self):
        pass


if __name__ == '__main__':
    unittest.main()
