"""
@author: yrmt
@contact: butanoler@gmail.com
@file: f_02_线程锁.py
@time: 2019/8/23
"""
import time
from threading import Lock, Thread
from concurrent.futures import ThreadPoolExecutor

# GIL 与 threading.Lock :
# 相同点：都是控制当前进程中只又唯一线程运行
# 不同点: GIL-控制粒度更小，针对与行级。threading.Lock-人工控制，可以针对一个事务
number = 0


def fn(n):
    global number
    for _ in range(400000):
        number += 1


print(number)
with ThreadPoolExecutor(3) as executor:
    executor.map(fn, range(3))
print(number)
print('--------------------------------分隔线---------------------------')
number = 0
lock = Lock()


def fn1(n):
    global number
    lock.acquire()  # 加锁
    for _ in range(400000):
        number += 1
    lock.release()


print(number)
with ThreadPoolExecutor(3) as executor:
    executor.map(fn1, range(3))
print(number)
print('--------------------------------分隔线---------------------------')
