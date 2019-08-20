"""
@author: yrmt
@contact: butanoler@gmail.com
@file: e_01_闭包.py
@time: 2019/8/18
"""
import time


# https://en.wikipedia.org/wiki/Closure_(computer_programming)
# https://stackoverflow.com/questions/11408515/about-python-closure

# 闭包定义:
# 在一个外函数中定义了一个内函数，内函数里运用了外函数的临时变量，
# 并且外函数的返回值是内函数的引用。这样就构成了一个闭包。

# 优点:
# 外层函数初始化一些值保存下来，内函数可以直接使用
# 单例模式
# 模仿类，外层函数下执行的像__init__
# 快,频繁相同执行的可以只执行一次
def outer(x):  # 闭包
    x = x if x >= 0 else -x

    def inner(y):
        return x + y

    return inner


def outer2(x, y):  # 非闭包
    x = x if x >= 0 else -x
    return x + y


start_time = time.time()
inr = outer(-4)
for i in range(1024 * 1024):
    inr(10)
print("outer :{}".format(time.time() - start_time))  # outer :1.3586533069610596

start_time = time.time()
for i in range(1024 * 1024):
    inr = outer2(-4, 10)
print("outer2 :{}".format(time.time() - start_time))  # outer2 :1.9085211753845215
