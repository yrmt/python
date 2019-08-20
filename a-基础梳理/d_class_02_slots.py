# -*- coding: utf-8 -*-
"""
@author: yrmt
@contact: butanoler@gmail.com
@file: d_class_02_slots.py
@time: 2019/8/16
"""


# slots -> http://book.pythontips.com/en/latest/__slots__magic.html

class A(object):
    __slots__ = ['a', 'b']

    def __init__(self):
        self.a = 'aaa'
        self.b = 'bbb'


class _A(object):
    def __init__(self):
        self.a = 'aaa'
        self.b = 'bbb'


try:
    a = A()
    a.c = 'c'
except AttributeError as ae:
    print(ae)
print('--------------------------------split---------------------------')


@profile
def test_a():
    x = [A() for _ in range(10240)]
    import time
    start_time = time.time()
    for tmp in x:
        t = tmp.a
        tt = tmp.b
    print('time1: {}'.format(time.time() - start_time))
    start_time = time.time()
    y = [_A() for _ in range(10240)]
    for tmp in y:
        t = tmp.a
        tt = tmp.b
    print('time2: {}'.format(time.time() - start_time))


"""
pip install memory-profiler
python -m memory_profiler c-class-01-slots.py

Filename: c-class-01-slots.py

Line #    Mem usage    Increment   Line Contents
================================================
    33   16.559 MiB   16.559 MiB   @profile
    34                             def test_a():
    35   17.148 MiB    0.062 MiB       x = [A() for _ in range(10240)]
    36   18.918 MiB    0.062 MiB       y = [_A() for _ in range(10240)]
    
time1: 0.7403461933135986
time2: 1.000784158706665
"""
test_a()
