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


class TestTiduManjian(unittest.TestCase):

    """
    设置产品数量2+。满20-5   梯度满减
    """
    def setUp(self):
        self.url = 'http://test.wgmf.com/promotion-online/online/validActivity'

    def test_get_activity(self):

        # 满20减5

        post_data = {
            "activityId": 0,
            "cusId": "16788112",
            "exchangeCode": "",
            "openId": "",
            "orderContext": {
                "proList": [
                    {
                        "code": "8",
                        "id": 8,
                        "name": "桃仁阿胶糕8",
                        "num": "2",
                        "price": 10,
                        "proImage": "string",
                        "skuName": "桃仁阿胶糕8",
                        "specialPrice": 0,
                        "templateId": "8",
                        "wareHouseCode": "555"
                    }
                ]
            },
            "phone": "string"
        }

        res = requests.post(url=self.url, json=post_data)

        res_dict = json.loads(res.text)

        activityId = res_dict['resultInfo'][0]['activityInfo']['activityId']
        giftmoney = res_dict['resultInfo'][0]['giftRuleResultContext']['giftMoney']

        self.assertEqual(activityId,6452, msg="结果不匹配")
        self.assertEqual(giftmoney,5,msg="减少金额应该是5")


        # 订单金额20，数量下于2

        post_data = {
            "activityId": 0,
            "cusId": "16788112",
            "exchangeCode": "",
            "openId": "",
            "orderContext": {
                "proList": [
                    {
                        "code": "8",
                        "id": 8,
                        "name": "桃仁阿胶糕8",
                        "num": "1",
                        "price": 20,
                        "proImage": "string",
                        "skuName": "桃仁阿胶糕8",
                        "specialPrice": 0,
                        "templateId": "8",
                        "wareHouseCode": "555"
                    }
                ]
            },
            "phone": "string"
        }

        res = requests.post(url=self.url, json=post_data)

        res_dict = json.loads(res.text)

        activity_list = res_dict['resultInfo']
        print(activity_list)

        self.assertEqual(len(activity_list),0,msg="活动信息列表应该为空")

        # 数量2+，订单金额不满20

        post_data = {
            "activityId": 0,
            "cusId": "16788112",
            "exchangeCode": "",
            "openId": "",
            "orderContext": {
                "proList": [
                    {
                        "code": "8",
                        "id": 8,
                        "name": "桃仁阿胶糕8",
                        "num": "2",
                        "price": 8,
                        "proImage": "string",
                        "skuName": "桃仁阿胶糕8",
                        "specialPrice": 0,
                        "templateId": "8",
                        "wareHouseCode": "555"
                    }
                ]
            },
            "phone": "string"
        }

        res = requests.post(url=self.url, json=post_data)

        res_dict = json.loads(res.text)

        activity_list = res_dict['resultInfo']

        self.assertEqual(len(activity_list),0,msg="活动信息列表应该为空")


        # 满40减10  梯度满减

        post_data = {
            "activityId": 0,
            "cusId": "16788112",
            "exchangeCode": "",
            "openId": "",
            "orderContext": {
                "proList": [
                    {
                        "code": "8",
                        "id": 8,
                        "name": "桃仁阿胶糕8",
                        "num": "2",
                        "price": 20,
                        "proImage": "string",
                        "skuName": "桃仁阿胶糕8",
                        "specialPrice": 0,
                        "templateId": "8",
                        "wareHouseCode": "555"
                    }
                ]
            },
            "phone": "string"
        }

        res = requests.post(url=self.url, json=post_data)

        res_dict = json.loads(res.text)

        activityId = res_dict['resultInfo'][0]['activityInfo']['activityId']
        giftmoney = res_dict['resultInfo'][0]['giftRuleResultContext']['giftMoney']

        self.assertEqual(activityId,6452, msg="结果不匹配")
        self.assertEqual(giftmoney,10,msg="减少金额应该是10")





        # 满60减15  梯度满减

        post_data = {
            "activityId": 0,
            "cusId": "16788112",
            "exchangeCode": "",
            "openId": "",
            "orderContext": {
                "proList": [
                    {
                        "code": "8",
                        "id": 8,
                        "name": "桃仁阿胶糕8",
                        "num": "3",
                        "price": 25,
                        "proImage": "string",
                        "skuName": "桃仁阿胶糕8",
                        "specialPrice": 0,
                        "templateId": "8",
                        "wareHouseCode": "555"
                    }
                ]
            },
            "phone": "string"
        }

        res = requests.post(url=self.url, json=post_data)

        res_dict = json.loads(res.text)

        activityId = res_dict['resultInfo'][0]['activityInfo']['activityId']
        giftmoney = res_dict['resultInfo'][0]['giftRuleResultContext']['giftMoney']

        self.assertEqual(activityId,6452, msg="结果不匹配")
        self.assertEqual(giftmoney,15,msg="减少金额应该是15")
    def tearDown(self):
        pass


if __name__ == '__main__':
    unittest.main()
