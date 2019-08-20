"""
@author: yrmt
@contact: butanoler@gmail.com
@file: e_02_注解.py
@time: 2019/8/18
"""


# 基础版 ----------------------
def _a(func):
    print("this is _a 。func:{}".format(func))

    def __a(*args, **kwargs):
        print("this is __a : args:{},kwargs:{}".format(args, kwargs))
        res = func(*args, **kwargs)
        print("this is __a end res:{}".format(res))
        return res

    return __a


@_a  # 1.在执行前会调用 _a(fn_a)获取该注解执行方法 得到 __a。(这步在即使不调用该方法也会执行)
def fn_a(name, age=18):
    print("this is fn_a")


print("fn_a 函数执行前")
# 2.调用该方法  此时会根据注解得到的__a方法句柄，执行__a(*args, **kwargs) -> __a('butanoler', age=19)
fn_a('butanoler', age=19)
print('--------------------------------分隔线---------------------------')


# 注解带方法 ----------------------
def b(log_format='id-day-msg'):
    print("this is b log_format:{}".format(log_format))

    def _b(func):
        print("this is _b 。func:{}".format(func))

        def __b(*args, **kwargs):
            print("this is __b : args:{},kwargs:{}".format(args, kwargs))
            res = func(*args, **kwargs)
            print("this is __b end res:{}".format(res))
            return res

        return __b

    return _b


# 在执行前先会调用 (这步在即使不调用该方法也会执行)
# 1. b(log_format='day-id-msg')  得到_b方法句柄
# 2. 再同上_b(fn_b)获取该注解执行方法 得到 __b
@b(log_format='day-id-msg')
def fn_b(name, age=18):
    print("this is fn_b")


print("fn_b 函数执行前")
# 2.调用该方法  此时会根据注解得到的__b方法句柄，执行__b(*args, **kwargs) -> __b('butanoler', age=19)
fn_b('butanoler', age=19)
print('--------------------------------分隔线---------------------------')


# 类注解方法(注解带方法变种)
class C(object):
    def __init__(self, log_format):
        print("this is C.__int__")
        self.log_format = log_format

    def __call__(self, func):
        print("this is C.__call__({})".format(func))

        def _c(*args, **kwargs):
            print("this is __c : args:{},kwargs:{}".format(args, kwargs))
            res = func(*args, **kwargs)
            print("this is __c end res:{}".format(res))
            return res

        return _c


# 在执行前先会调用 (这步在即使不调用该方法也会执行)
# 1. C(log_format='day-id-msg')  C类的实例化属性
# 2. 再同上 C类的实例化属性(fn_c) -> C类的实例化属性.__call__(fn_c) 返回_c方法
@C(log_format='day-id-msg')
def fn_c(name, age=18):
    print("this is fn_c")


print("fn_c 函数执行前")
# 2.调用该方法  此时会根据注解得到的_c方法句柄，执行_c(*args, **kwargs) -> _c('butanoler', age=19)
fn_c('butanoler', age=19)
