"""
@author: yrmt
@contact: butanoler@gmail.com
@file: f_01_生成器.py
@time: 2019/8/19
"""
# 了解即可
# https://wiki.python.org/moin/Generators
# https://docs.python.org/3/reference/expressions.html#yield-expressions

print(range(10))  # 生成器
print(list(range(10)))  # 数组
print('--------------------------------分隔线---------------------------')


# 全部生成
def a(n):
    num = 0
    nums = []
    while num < n:
        nums.append(num)
        num += 1
    return nums


# 类方法
class B(object):
    def __init__(self, num):
        self.num = num
        self.index = 0

    def __iter__(self):
        self.index = 0
        return self

    def __next__(self):
        if self.num > self.index:
            tmp = self.index
            self.index += 1
            return tmp
        else:
            raise StopIteration()


# yield 方法
def c(n):
    num = 0
    while num < n:
        yield num
        num += 1


print(c(10))  # 生成器 <generator object c at 0x000002B9963A17C8>
print(sum(a(10000)))
print(sum(B(10000)))
print(sum(c(10000)))
print('--------------------------------分隔线---------------------------')


def d(n):
    num = 0
    print("start while")
    while num < n:
        print("yield 之前")
        yield num
        print("yield 之后")
        num += 1


gen = d(2)  # 调用方法什么都不执行 返回一个生成器
print("step 1")
print(next(gen))  # 调用next,执行到第一次遇到yield,并会返回yield的值
print("step 2")
print(next(gen))  # 再次调用next,执行到第二次遇到yield,并会返回yield的值
print("step 3")
try:
    print(next(gen))  # 再次调用next,执行到第三次遇到yield,但此时没有yield,所以会扔出 StopIteration
except StopIteration:
    print("this is StopIteration")
print('--------------------------------分隔线---------------------------')


def e():
    print("start while")
    print("yield1 之前")
    value = yield 1
    print("value: ", value)
    print("yield1 之后")
    print("yield2 之前")
    yield 2
    print("yield2 之后")
    yield 3


gen_e = e()
print("step 1")
print(next(gen_e))
print("step 2")
print(gen_e.send(12))  # 再 send 时 会将该值 传入 value 中
print("step 3")
print('--------------------------------分隔线---------------------------')


# yield from
def g():
    yield 2
    yield 3


def f():
    value = yield g()
    print("value: ", value)
    value2 = yield from g()
    print("value2: ", value2)
    yield 4


gen_f = f()
print("step 1")
print(next(gen_f))  # 如果不是yield from 则会返回一个生成器
print("step 2")
print(next(gen_f))  # 返回生成器值,并迭代该生成器
print("step 3")
print(next(gen_f))
print("step 4")
