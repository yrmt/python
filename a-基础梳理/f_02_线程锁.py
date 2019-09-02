"""
@author: yrmt
@contact: butanoler@gmail.com
@file: f_02_线程锁.py
@time: 2019/8/23
"""
from threading import Lock, RLock
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


def sisuo():
    lock_01 = Lock()
    print("start lock01 -acquire 1")
    lock_01.acquire()
    print("start lock01 -acquire 2")
    lock_01.acquire()  # 当第二次调用 acquire 时会等待第一次解锁，程序会卡死
    print("start lock01 -acquire 3")


# sisuo()  # 看效果调用
print('--------------------------------分隔线---------------------------')
r_lock = RLock()  # rlock 调用多少次 acquire 就需要调用释放多少次


def suo_02():
    print("start lock01 -acquire 1")
    r_lock.acquire()
    print("start lock01 -acquire 2")
    r_lock.acquire()
    print("start lock01 -acquire 3")


suo_02()
