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
from mock import mock
from conf.mymock import mock_test


class TestVipActivity(unittest.TestCase):
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

        res = mock_test(requests.post,post_data,self.url,'post',post_data)

        print(res)

        #mock_data = mock.Mock(return_value=post_data)


        #requests.post = mock_data

        #res = requests.post(url=self.url, json=post_data)

        #res_dict = json.loads(res.text)
        #print(res_dict)

        # activity_list = []
        #
        # for activity in res_dict['resultInfo']:
        #     activity_list.append(activity['activityInfo']['activityId'])
        #
        # self.assertEqual(activity_list, [6450, 6447], msg="结果不匹配")

        # # 9满不减
        #
        #
        # post_data = {
        #     "activityId": 0,
        #     "cusId": "16788112",
        #     "exchangeCode": "",
        #     "openId": "",
        #     "orderContext": {
        #         "proList": [
        #             {
        #                 "code": "9",
        #                 "name": "中宁枸杞初心蜜",
        #                 "num": "2",
        #                 "price": 4,
        #                 "proImage": "string",
        #                 "skuName": "规格",
        #                 "specialPrice": 0,
        #                 "templateId": "9",
        #                 "wareHouseCode": "666"
        #             }
        #         ]
        #     },
        #     "phone": "string"
        # }
        #
        # res = requests.post(url=self.url, json=post_data)
        #
        # res_dict = json.loads(res.text)
        #
        # activity_list = []
        #
        # for activity in res_dict['resultInfo']:
        #     activity_list.append(activity['activityInfo']['activityId'])
        #
        # self.assertEqual(activity_list, [], msg="结果不匹配")
        #
        # # 产品8 满15 送枸杞
        #
        #
        #
        # post_data = {
        #     "activityId": 0,
        #     "cusId": "686000660",
        #     "exchangeCode": "",
        #     "openId": "",
        #     "orderContext": {
        #         "proList": [
        #             {
        #                 "code": "8",
        #                 "id": 8,
        #                 "name": "桃仁阿胶糕8",
        #                 "num": "3",
        #                 "price": 5,
        #                 "proImage": "string",
        #                 "skuName": "桃仁阿胶糕8",
        #                 "specialPrice": 0,
        #                 "templateId": "8",
        #                 "wareHouseCode": "555"
        #             }
        #
        #         ]
        #     },
        #     "phone": "string"
        # }
        #
        # res = requests.post(url=self.url, json=post_data)
        #
        # res_dict = json.loads(res.text)
        #
        # activity_list = []
        #
        # for activity in res_dict['resultInfo']:
        #     # print(activity['activityInfo']['activityId'])
        #
        #     activity_list.append(activity['activityInfo']['activityId'])
        #
        # self.assertEqual(activity_list, [6450, 6449, 6447, 6445, 6324], msg="结果不匹配")
        #
        # # 产品8 满10
        #
        #
        #
        # post_data = {
        #     "activityId": 0,
        #     "cusId": "686000660",
        #     "exchangeCode": "",
        #     "openId": "",
        #     "orderContext": {
        #         "proList": [
        #             {
        #                 "code": "8",
        #                 "id": 8,
        #                 "name": "桃仁阿胶糕8",
        #                 "num": "2",
        #                 "price": 5,
        #                 "proImage": "string",
        #                 "skuName": "桃仁阿胶糕8",
        #                 "specialPrice": 0,
        #                 "templateId": "8",
        #                 "wareHouseCode": "555"
        #             }
        #
        #         ]
        #     },
        #     "phone": "string"
        # }
        #
        # res = requests.post(url=self.url, json=post_data)
        #
        # res_dict = json.loads(res.text)
        #
        # activity_list = []
        #
        # for activity in res_dict['resultInfo']:
        #     # print(activity['activityInfo']['activityId'])
        #
        #     activity_list.append(activity['activityInfo']['activityId'])
        #
        # self.assertEqual(activity_list, [6450, 6447, 6324], msg="结果不匹配")
        #
        # # 产品8 满<10
        #
        #
        #
        # post_data = {
        #     "activityId": 0,
        #     "cusId": "686000660",
        #     "exchangeCode": "",
        #     "openId": "",
        #     "orderContext": {
        #         "proList": [
        #             {
        #                 "code": "8",
        #                 "id": 8,
        #                 "name": "桃仁阿胶糕8",
        #                 "num": "2",
        #                 "price": 4,
        #                 "proImage": "string",
        #                 "skuName": "桃仁阿胶糕8",
        #                 "specialPrice": 0,
        #                 "templateId": "8",
        #                 "wareHouseCode": "555"
        #             }
        #
        #         ]
        #     },
        #     "phone": "string"
        # }
        #
        # res = requests.post(url=self.url, json=post_data)
        #
        # res_dict = json.loads(res.text)
        #
        # activity_list = []
        #
        # for activity in res_dict['resultInfo']:
        #     #print(activity['activityInfo']['activityId'])
        #
        #     activity_list.append(activity['activityInfo']['activityId'])
        #
        # self.assertEqual(activity_list, [6324, ], msg="结果不匹配")
        #
        #
        #
        #
        # # 产品组合，产品7 2+ 10 -3
        #
        # post_data = {
        #     "activityId": 0,
        #     "cusId": "686000660",
        #     "exchangeCode": "",
        #     "openId": "",
        #     "orderContext": {
        #         "proList": [
        #
        #             {
        #                 "code": "7",
        #                 "name": "百年老树鲜核桃7",
        #                 "num": "1",
        #                 "price": 2,
        #                 "proImage": "string",
        #                 "skuName": "2斤装",
        #                 "specialPrice": 0,
        #                 "templateId": "7",
        #                 "wareHouseCode": "888"
        #             },
        #             {
        #                 "code": "9",
        #                 "name": "中宁枸杞初心蜜",
        #                 "num": "2",
        #                 "price": 4,
        #                 "proImage": "string",
        #                 "skuName": "规格",
        #                 "specialPrice": 0,
        #                 "templateId": "9",
        #                 "wareHouseCode": "666"
        #             }
        #
        #         ]
        #     },
        #     "phone": "string"
        # }
        #
        # res = requests.post(url=self.url, json=post_data)
        #
        # res_dict = json.loads(res.text)
        #
        # activity_list = []
        #
        # for activity in res_dict['resultInfo']:
        #     print(activity['activityInfo']['activityId'])
        #
        #     activity_list.append(activity['activityInfo']['activityId'])
        #
        # self.assertEqual(activity_list, [6446], msg="结果不匹配")

    def tearDown(self):
        pass


if __name__ == '__main__':
    unittest.main()
