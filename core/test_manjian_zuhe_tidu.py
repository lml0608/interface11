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


class TestManjianZuheTidu(unittest.TestCase):

    """
    设置满减活动产品组合，订单金额45
    产品9  数量2+
    产品组合，包含产品7 数量2+ 
    赠送金额15
    支持梯度
    """
    def setUp(self):
        self.url = 'http://test.wgmf.com/promotion-online/online/validActivity'

    def test_get_activity(self):



        #满45-15
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
                        "price": 8,
                        "proImage": "string",
                        "skuName": "规格",
                        "specialPrice": 0,
                        "templateId": "9",
                        "wareHouseCode": "666"
                    },
                    {
                        "code": "7",
                        "name": "百年老树鲜核桃7",
                        "num": "2",
                        "price": 10,
                        "proImage": "string",
                        "skuName": "2斤装",
                        "specialPrice": 0,
                        "templateId": "7",
                        "wareHouseCode": "888"
                    },
                    {
                        "code": "8",
                        "id": 8,
                        "name": "桃仁阿胶糕8",
                        "num": "1",
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

        #print(res_dict)

        activityId = res_dict['resultInfo'][0]['activityInfo']['activityId']
        giftmoney = res_dict['resultInfo'][0]['giftRuleResultContext']['giftMoney']

        self.assertEqual(len(res_dict['resultInfo']),1)

        self.assertEqual(activityId,6454, msg="结果不匹配")
        self.assertEqual(giftmoney,15,msg="减少金额应该是15")

        # 有产品9 没有组合产品

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
                    },
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

        activity_list = res_dict['resultInfo']

        self.assertEqual(len(activity_list),0,msg="活动信息列表应该为空")

        #有组合产品没有产品9

        post_data = {
            "activityId": 0,
            "cusId": "16788112",
            "exchangeCode": "",
            "openId": "",
            "orderContext": {
                "proList": [
                    {
                        "code": "7",
                        "name": "百年老树鲜核桃7",
                        "num": "3",
                        "price": 10,
                        "proImage": "string",
                        "skuName": "2斤装",
                        "specialPrice": 0,
                        "templateId": "7",
                        "wareHouseCode": "888"
                    },
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

        activity_list = res_dict['resultInfo']

        self.assertEqual(len(activity_list),0,msg="活动信息列表应该为空")


        #产品数量不符合



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
                        "num": "1",
                        "price": 30,
                        "proImage": "string",
                        "skuName": "规格",
                        "specialPrice": 0,
                        "templateId": "9",
                        "wareHouseCode": "666"
                    },
                    {
                        "code": "7",
                        "name": "百年老树鲜核桃7",
                        "num": "2",
                        "price": 10,
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

        res = requests.post(url=self.url, json=post_data)

        res_dict = json.loads(res.text)

        activity_list = res_dict['resultInfo']

        self.assertEqual(len(activity_list),0,msg="活动信息列表应该为空")



        #组合数量不符合



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
                        "price": 15,
                        "proImage": "string",
                        "skuName": "规格",
                        "specialPrice": 0,
                        "templateId": "9",
                        "wareHouseCode": "666"
                    },
                    {
                        "code": "7",
                        "name": "百年老树鲜核桃7",
                        "num": "1",
                        "price": 25,
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

        res = requests.post(url=self.url, json=post_data)

        res_dict = json.loads(res.text)

        activity_list = res_dict['resultInfo']

        self.assertEqual(len(activity_list),0,msg="活动信息列表应该为空")

        #订单金额不符合条件


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
                        "price": 5,
                        "proImage": "string",
                        "skuName": "规格",
                        "specialPrice": 0,
                        "templateId": "9",
                        "wareHouseCode": "666"
                    },
                    {
                        "code": "7",
                        "name": "百年老树鲜核桃7",
                        "num": "3",
                        "price": 8,
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

        res = requests.post(url=self.url, json=post_data)

        res_dict = json.loads(res.text)

        activity_list = res_dict['resultInfo']

        self.assertEqual(len(activity_list),0,msg="活动信息列表应该为空")


        #组合金额不符合条件


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
                        "price": 15,
                        "proImage": "string",
                        "skuName": "规格",
                        "specialPrice": 0,
                        "templateId": "9",
                        "wareHouseCode": "666"
                    },
                    {
                        "code": "7",
                        "name": "百年老树鲜核桃7",
                        "num": "3",
                        "price": 6,
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

        res = requests.post(url=self.url, json=post_data)

        res_dict = json.loads(res.text)

        activity_list = res_dict['resultInfo']

        self.assertEqual(len(activity_list),0,msg="活动信息列表应该为空")




        #梯度满减90-30


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
                        "price": 15,
                        "proImage": "string",
                        "skuName": "规格",
                        "specialPrice": 0,
                        "templateId": "9",
                        "wareHouseCode": "666"
                    },
                    {
                        "code": "7",
                        "name": "百年老树鲜核桃7",
                        "num": "2",
                        "price": 15,
                        "proImage": "string",
                        "skuName": "2斤装",
                        "specialPrice": 0,
                        "templateId": "7",
                        "wareHouseCode": "888"
                    },
                    {
                        "code": "8",
                        "id": 8,
                        "name": "桃仁阿胶糕8",
                        "num": "4",
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

        #print(res_dict)

        activityId = res_dict['resultInfo'][0]['activityInfo']['activityId']
        giftmoney = res_dict['resultInfo'][0]['giftRuleResultContext']['giftMoney']

        self.assertEqual(len(res_dict['resultInfo']),1)

        self.assertEqual(activityId,6454, msg="结果不匹配")
        self.assertEqual(giftmoney,30,msg="减少金额应该是30")


        #梯度满减1 - 45



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
                        "num": "4",
                        "price": 15,
                        "proImage": "string",
                        "skuName": "规格",
                        "specialPrice": 0,
                        "templateId": "9",
                        "wareHouseCode": "666"
                    },
                    {
                        "code": "7",
                        "name": "百年老树鲜核桃7",
                        "num": "2",
                        "price": 15,
                        "proImage": "string",
                        "skuName": "2斤装",
                        "specialPrice": 0,
                        "templateId": "7",
                        "wareHouseCode": "888"
                    },
                    {
                        "code": "8",
                        "id": 8,
                        "name": "桃仁阿胶糕8",
                        "num": "5",
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

        #print(res_dict)

        activityId = res_dict['resultInfo'][0]['activityInfo']['activityId']
        giftmoney = res_dict['resultInfo'][0]['giftRuleResultContext']['giftMoney']

        self.assertEqual(len(res_dict['resultInfo']),1)

        self.assertEqual(activityId,6454, msg="结果不匹配")
        self.assertEqual(giftmoney,45,msg="减少金额应该是")

    def tearDown(self):
        pass


if __name__ == '__main__':
    unittest.main()
