"""
@author: yrmt
@contact: butanoler@gmail.com
@file: d_class_06_实例化.py
@time: 2019/8/18
"""


# __new__ :新实例的创建
# __init__:新实例的初始化
# 实例创建 :
# 1. __new__ 返回类的新实例
# 2. __ init__ 初始化 (不会返回任何内容, 第一个参数即为new的返回值)

class A(object):
    def __init__(self, name):
        self.name = name
        print("this is A.__init__({})".format(name))

    # 没加上classmethod 的classmethod方法
    def __new__(cls, *args, **kwargs):
        print("this is A.__new__({},{})".format(args, kwargs))
        return object.__new__(cls)


class B(A):
    def __init__(self, name):
        super().__init__(name)
        print("this is B.__init__({})".format(name))

    # 没加上classmethod 的classmethod方法
    def __new__(cls, *args, **kwargs):
        print("this is B.__new__({},{})".format(args, kwargs))
        return super().__new__(cls)


a = A("butanoler")
print(a.__dict__)
print(A.__dict__)
print('--------------------------------分隔线---------------------------')
b = B("butanoler")
print(b.__dict__)
print(B.__dict__)
