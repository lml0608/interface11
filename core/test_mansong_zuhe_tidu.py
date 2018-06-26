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


class TestManSongZuheTidu(unittest.TestCase):

    """ 
    产品7 2+   组合金额10
    赠品5 数量1 
    订单金额15
    梯度满赠
    """
    def setUp(self):
        self.url = 'http://test.wgmf.com/promotion-online/online/validActivity'

    def test_get_activity(self):

        # 满足条件

        #产品7数量小于2
        #产品组合金额小于10
        #订单金额小于15
        #没有产品7

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
                        "num": "2",
                        "price": 5,
                        "proImage": "string",
                        "skuName": "2斤装",
                        "specialPrice": 0,
                        "templateId": "7",
                        "wareHouseCode": "888"
                    },
                    {
                        "code": "9",
                        "name": "中宁枸杞初心蜜",
                        "num": "2",
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
        #活动ID
        activityId = res_dict['resultInfo'][0]['activityInfo']['activityId']
        #赠品ID
        giftcode = res_dict['resultInfo'][0]['giftRuleResultContext']['giftProductInfo'][0]['code']
        #赠品数量
        giftnum = res_dict['resultInfo'][0]['giftRuleResultContext']['giftProductInfo'][0]['num']

        self.assertEqual(activityId,6456, msg="结果不匹配")
        self.assertEqual(giftcode,'5',msg="赠品ID=5")
        self.assertEqual(giftnum,'1',msg='赠品数量为1')


        #订单金额满15，产品2+
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
                        "price": 3,
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
        #活动ID
        activityId = res_dict['resultInfo'][0]['activityInfo']['activityId']
        #赠品ID
        giftcode = res_dict['resultInfo'][0]['giftRuleResultContext']['giftProductInfo'][0]['code']
        #赠品数量
        giftnum = res_dict['resultInfo'][0]['giftRuleResultContext']['giftProductInfo'][0]['num']

        self.assertEqual(activityId,6456, msg="结果不匹配")
        self.assertEqual(giftcode,'5',msg="赠品ID=5")
        self.assertEqual(giftnum,'1',msg='赠品数量为1')

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



        # 产品9数量小于2
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
                        "price": 3,
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
        activity_list = res_dict['resultInfo']
        self.assertEqual(len(activity_list),0,msg="活动信息列表应该为空")




        # 订单金额小于15
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
                        "price": 3,
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
                        "price": 4,
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



        #梯度满赠，30 送2份


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
                    },
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
        # 活动ID
        activityId = res_dict['resultInfo'][0]['activityInfo']['activityId']
        # 赠品ID
        giftcode = res_dict['resultInfo'][0]['giftRuleResultContext']['giftProductInfo'][0]['code']
        # 赠品数量
        giftnum = res_dict['resultInfo'][0]['giftRuleResultContext']['giftProductInfo'][0]['num']

        self.assertEqual(activityId, 6456, msg="结果不匹配")
        self.assertEqual(giftcode, '5', msg="赠品ID=5")
        self.assertEqual(giftnum, '2', msg='赠品数量为2')


        #梯度满赠，45 送3份


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
                        "num": "5",
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
        # 活动ID
        activityId = res_dict['resultInfo'][0]['activityInfo']['activityId']
        # 赠品ID
        giftcode = res_dict['resultInfo'][0]['giftRuleResultContext']['giftProductInfo'][0]['code']
        # 赠品数量
        giftnum = res_dict['resultInfo'][0]['giftRuleResultContext']['giftProductInfo'][0]['num']

        self.assertEqual(activityId, 6456, msg="结果不匹配")
        self.assertEqual(giftcode, '5', msg="赠品ID=5")
        self.assertEqual(giftnum, '3', msg='赠品数量为3')

        #


    def tearDown(self):
        pass


if __name__ == '__main__':
    unittest.main()
