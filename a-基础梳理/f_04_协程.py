"""
@author: yrmt
@contact: butanoler@gmail.com
@file: f_04_协程.py
@time: 2019/9/2
"""
import asyncio
import time


# https://stackoverflow.com/questions/49005651/how-does-asyncio-actually-work/51116910#51116910

# 协程关键字 async def
# 迭代器实现时通过 __iter__ , 协程实现 __await__ ,
# 迭代器层次实现 yield,yield from ， 协程 await

async def a_01():  # python3的写法
    print("this is a_01 start")
    await asyncio.sleep(1)
    print("this is a_01 end")


@asyncio.coroutine
def a_02():
    print("this is a_02 start")
    yield from asyncio.sleep(1)
    print("this is a_02 end")


loop = asyncio.get_event_loop()
task = [a_01(), a_02()]
print("start all")
loop.run_until_complete(asyncio.wait(task))
loop.close()

print('--------------------------------分隔线---------------------------')


def b_01():
    while True:
        print("this is b_01 sleep")
        time.sleep(2)
        print("this is b_01 start")
        yield
        print("this is b_01 end")


def b_02():
    while True:
        print("this is b_02 sleep")
        time.sleep(2)
        print("this is b_02 start")
        yield
        print("this is b_02 end")


def b():
    b01 = b_01()
    b02 = b_02()
    for i in range(3):
        next(b01)
        next(b02)


b()
print('--------------------------------分隔线---------------------------')
