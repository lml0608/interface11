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
    产品9 1+
    赠品5 数量1
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
                        "num": "1",
                        "price": 2,
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

        self.assertEqual(activityId,6455, msg="结果不匹配")
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
        activity_list = res_dict['resultInfo']
        self.assertEqual(len(activity_list),0,msg="活动信息列表应该为空")

    def tearDown(self):
        pass


if __name__ == '__main__':
    unittest.main()
