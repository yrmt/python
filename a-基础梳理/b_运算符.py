"""
@author: yrmt
@contact: butanoler@gmail.com
@file: b_运算符.py
@time: 2019/8/14
"""
a = 5
b = 3
print("除运算:", a / b)
print("整除运算(向下取整)", a // b)
print("乘运算", a * b)
print("幂运算", a ** b)
print('--------------------------------分隔线---------------------------')


class A(object):
    def __init__(self, name):
        self.name = name

    def __eq__(self, other):
        print("__eq__", end=':')
        if not isinstance(other, A):
            return False
        if other.name == self.name:
            return True
        return False


ba = A('a')
bb = A('a')
print("ba == bb:", ba == bb)  # 值判断 调用 __eq__
print("ba is bb:", ba is bb)  # 地址判断
print('--------------------------------分隔线---------------------------')

# !!! 字符串驻留机制
ca = 'a_'
cb = 'a_'
print('ca == cb:', ca == cb)  # 值判断
print('ca is cb:', ca is cb)  # 地址判断
print('--------------------------------分隔线---------------------------')

da = 'a_' * 2100
db = 'a_' * 2100
print('da == db:', da == db)  # 长 值判断
print('da is db:', da is db)  # 地址判断
print('--------------------------------分隔线---------------------------')

ea = 'a_#'
eb = 'a_#'
print('ea == eb:', ea == eb)  # 值判断 在客户端中为false, (只存在数字字母下划线)
print('ea is eb:', ea is eb)  # 地址判断
print('--------------------------------分隔线---------------------------')

# 整数问题
fa = -6
fb = -6
print("fa == fb:", fa == fb)  # 值判断
print("fa is fb:", fa is fb)  # 地址判断 在客户端中为false ( 客户端: [-5,256] ,文件启动: [-5,正无穷] )
print('--------------------------------分隔线---------------------------')

ga = 25
gb = 25
print("ga == gb:", ga == gb)  # 值判断
print("ga is gb:", ga is gb)  # 地址判断 在客户端中为false
print('--------------------------------分隔线---------------------------')

ha = 257
hb = 257
print("ha == hb:", ha == hb)  # 值判断
print("ha is hb:", ha is hb)  # 地址判断 在客户端中为false
print('--------------------------------分隔线---------------------------')
