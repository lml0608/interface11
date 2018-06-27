# -*- coding:utf-8 -*-  
'''
__author__:liubin 

'''

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


class Paixu(unittest.TestCase):

    """
    
    6472,6473, 6468, 6469, 6467, 6471, 6475, 6474, 6470, 6470, 6470, 6477, 6476
    """
    def setUp(self):
        self.url = 'http://test.wgmf.com/promotion-online/online/validActivity'

    def test_get_activity(self):


        #满减
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
                        "code": "7",
                        "name": "百年老树鲜核桃7",
                        "num": "2",
                        "price": 5,
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

        activity_list = []
        for acticity in res_dict['resultInfo']:
            activity_list.append(acticity['activityInfo']['activityId'])



        #活动ID
        # activityId_1 = res_dict['resultInfo'][0]['activityInfo']['activityId']
        # activityId_2 = res_dict['resultInfo'][1]['activityInfo']['activityId']

        #
        # self.assertEqual(activityId_1,6468, msg="结果不匹配")
        # self.assertEqual(activityId_2,6469, msg="结果不匹配")

        #self.assertEqual(activity_list,[6472,6473, 6468, 6469, 6467, 6471, 6475, 6474, 6470, 6470, 6470, 6477, 6476])



        #满赠



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
                        "num": "6",
                        "price": 9,
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

        activity_list = []
        for acticity in res_dict['resultInfo']:


            activity_list.append(acticity['activityInfo']['activityId'])

        print(activity_list)

        # 活动ID
        # activityId_1 = res_dict['resultInfo'][0]['activityInfo']['activityId']
        # activityId_2 = res_dict['resultInfo'][1]['activityInfo']['activityId']

        #
        # self.assertEqual(activityId_1,6468, msg="结果不匹配")
        # self.assertEqual(activityId_2,6469, msg="结果不匹配")

        #self.assertEqual(activity_list, [6472, 6473, 6468, 6469, 6467, 6471, 6475, 6474, 6470, 6470, 6470, 6477, 6476])

    def tearDown(self):
        pass


if __name__ == '__main__':
    unittest.main()
