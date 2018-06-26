# -*- coding:utf-8 -*-  
'''
__author__:liubin 

'''

list1 = [1,2]
list2 = [1,2]

print(id(list1))

print(id(list2))
import operator
#
# a = [1, -1, 0]
# b = [1, -1, 0]
# c = [-1, 1, 0]
print(operator.eq(list1, list2))
#print(operator.eq(a, c))