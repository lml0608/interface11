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
    套餐sku ,7,8
    """

    def setUp(self):
        self.url = 'http://test.wgmf.com/promotion-online/online/package'

    def test_get_activity(self):

        # 使用2个sku请求
        res = requests.get(url=self.url, params={'proId': '7,8'})
        res_dict = json.loads(res.text)

        activityId = res_dict['resultInfo'][0]['activityId']

        #print(activityId)

        self.assertEqual(activityId, 6463)

        # 使用，7，8,2请求

        res = requests.get(url=self.url, params={'proId': '7,8,210'})
        res_dict = json.loads(res.text)

        activity_list = res_dict['resultInfo']
        self.assertEqual(len(activity_list),0,msg="活动信息列表应该为空")


        #7,4 返回活动大的

        res = requests.get(url=self.url, params={'proId': '7,4'})
        res_dict = json.loads(res.text)

        #
        # activityId = res_dict['resultInfo'][0]['activityId']
        #
        # #print(activityId)
        #
        # self.assertEqual(activityId, 6463)



        #存在多个满足条件的活动时，返回活动ID大的
        res = requests.get(url=self.url, params={'proId': '7'})
        res_dict = json.loads(res.text)

        activityId = res_dict['resultInfo'][0]['activityId']

        #print(activityId)

        self.assertEqual(activityId, 6463)

        #SKU个数小于活动SKU个数,查询不出结果
        res = requests.get(url=self.url, params={'proId': '4,8'})
        res_dict = json.loads(res.text)

        activity_list = res_dict['resultInfo']
        self.assertEqual(len(activity_list),0,msg="活动信息列表应该为空")


        #多个SKU
        res = requests.get(url=self.url, params={'proId': '4,8,18'})
        res_dict = json.loads(res.text)

        activityId = res_dict['resultInfo'][0]['activityId']


        self.assertEqual(activityId, 6461)


        #多个SKU
        res = requests.get(url=self.url, params={'proId': '38,18'})
        res_dict = json.loads(res.text)

        activityId = res_dict['resultInfo'][0]['activityId']


        self.assertEqual(activityId, 6457)

        #多个SKU
        res = requests.get(url=self.url, params={'proId': '4,8'})
        res_dict = json.loads(res.text)
        activity_list = res_dict['resultInfo']
        self.assertEqual(len(activity_list),0,msg="活动信息列表应该为空")


        res = requests.get(url=self.url, params={'proId': '7,4'})
        res_dict = json.loads(res.text)

        activityId = res_dict['resultInfo'][0]['activityId']


        self.assertEqual(activityId, 6462)


        res = requests.get(url=self.url, params={'proId': '4'})
        res_dict = json.loads(res.text)

        activityId = res_dict['resultInfo'][0]['activityId']


        self.assertEqual(activityId, 6462)


        res = requests.get(url=self.url, params={'proId': '18'})
        res_dict = json.loads(res.text)

        activityId = res_dict['resultInfo'][0]['activityId']


        self.assertEqual(activityId, 6461)





    def tearDown(self):
        pass


if __name__ == '__main__':
    unittest.main()
