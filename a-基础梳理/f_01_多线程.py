"""
@author: yrmt
@contact: butanoler@gmail.com
@file: f_01_多线程.py
@time: 2019/8/19
"""
import time
from threading import Thread, Lock
import threading
from concurrent.futures import ThreadPoolExecutor


# 多线程 (操作系统决定如何切换python外部的任务,处理器数量1)
# CPU密集型 因为GIL锁，所以可能为线性
# IO密集型, 并发处理


def countdown(n):
    print(threading.get_ident(), " start")
    while n > 0:
        n -= 1
    print(threading.get_ident(), " end")


def a_1():
    count = 50000000
    start = time.time()
    countdown(count)
    end = time.time()
    print(end - start)


def a_2():
    count = 50000000
    t1 = Thread(target=countdown, args=(count / 2,))
    t2 = Thread(target=countdown, args=(count / 2,))
    start = time.time()
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    end = time.time()
    print(end - start)


# 花费大量时间等待外部事件的任务通常是线程化的良好候选者。
# 需要大量CPU计算并且花费很少时间等待外部事件的问题可能根本不会运行得更快。
a_1()  # 1.9305393695831299
a_2()  # 2.2978527545928955
print('--------------------------------分隔线---------------------------')


# 另一种实现 ,和java 一样
class A(Thread):
    def run(self) -> None:
        countdown(50000000 / 2)


start = time.time()
a = A()
b = A()
a.start()
b.start()
a.join()
b.join()
end = time.time()
print(end - start)
print('--------------------------------分隔线---------------------------')

with ThreadPoolExecutor(3) as executer:
    executer.map(countdown, range(10))
print('--------------------------------分隔线---------------------------')
