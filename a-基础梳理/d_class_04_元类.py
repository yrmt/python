"""
@author: yrmt
@contact: butanoler@gmail.com
@file: c_class_04_元类.py
@time: 2019/8/17
"""


# metaclasses : 元类
# https://www.python.org/dev/peps/pep-3115/
# https://stackoverflow.com/questions/100003/what-are-metaclasses-in-python
class A(object): pass


a = A()
print(type(A))  # A 类型为type，是类对象。
print(type(a))  # a 类型为A，是实例对象。
print('--------------------------------分隔线---------------------------')


@staticmethod
def bb_static():
    print("bb_static")


@classmethod
def bb_class(cls):
    print("bb_class :{}".format(cls))


def bb_func(slef):
    print("bb_func :{}".format(slef))


# 创建类对象
B = type('B', (A,), {'bb_static': bb_static, 'bb_class': bb_class, 'bb_func': bb_func})
print(B.mro())  # 类的继承关系
print(B.__dict__)  # 查看类中绑定的东西
B.bb_static()  # 静态方法
B.bb_class()  # 类方法
B().bb_func()  # 实例方法

