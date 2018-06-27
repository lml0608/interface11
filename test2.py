# -*- coding:utf-8 -*-  
'''
__author__:liubin 

'''


import requests


# s = requests.Session()
#
# s.get('http://httpbin.org/cookies/set/sessioncookie/123456789')
#
# r = s.get("http://httpbin.org/cookies")
#
# print(r.text)

s = requests.Session()
s.auth = ('user', 'pass')
s.headers.update({'x-test': 'true'})

# both 'x-test' and 'x-test2' are sent
r = s.get('http://httpbin.org/headers', headers={'x-test2': 'true'})

print(r.text)