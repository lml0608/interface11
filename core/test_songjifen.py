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


class TestManSong(unittest.TestCase):

    """
    产品9 2+
    2倍积分
    """
    def setUp(self):
        self.url = 'http://test.wgmf.com/promotion-online/online/validActivity'

    def test_get_activity(self):

        # 买9送5

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
                        "price": 6,
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
        #活动ID
        activityId = res_dict['resultInfo'][0]['activityInfo']['activityId']
        #赠送积分
        giftpoint = res_dict['resultInfo'][0]['giftRuleResultContext']['giftPoint']
        #赠送积分倍数
        multiplepoint = res_dict['resultInfo'][0]['giftRuleResultContext']['multiplePoint']

        self.assertEqual(activityId,6458, msg="结果不匹配")
        self.assertEqual(giftpoint,12,msg="赠送积分是12")
        self.assertEqual(multiplepoint,2,msg='积分倍数是2')

        #含有活动外的产品

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
                        "price": 6,
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

        print(res_dict)
        #活动ID
        activityId = res_dict['resultInfo'][0]['activityInfo']['activityId']
        #赠送积分
        giftpoint = res_dict['resultInfo'][0]['giftRuleResultContext']['giftPoint']
        #赠送积分倍数
        multiplepoint = res_dict['resultInfo'][0]['giftRuleResultContext']['multiplePoint']

        self.assertEqual(activityId,6458, msg="结果不匹配")
        self.assertEqual(giftpoint,12,msg="赠送积分是12")
        self.assertEqual(multiplepoint,2,msg='积分倍数是2')

        #初心密数量小于2
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
                        "price": 6,
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


        # 订单不包含产品9
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
        activity_list = res_dict['resultInfo']
        self.assertEqual(len(activity_list),0,msg="活动信息列表应该为空")

    def tearDown(self):
        pass


if __name__ == '__main__':
    unittest.main()
