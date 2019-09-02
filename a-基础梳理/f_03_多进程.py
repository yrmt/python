"""
@author: yrmt
@contact: butanoler@gmail.com
@file: f_03_多进程.py
@time: 2019/9/2
"""
import os
import time
from multiprocessing import Process, Pool


# 子进程要执行的代码
def run_proc(num):
    print('num:{},pid:{} start'.format(num, os.getpid()))
    time.sleep(num)
    print('num:{},pid:{} end'.format(num, os.getpid()))


def test_01():
    """基础用法"""
    print('当前进程号: {}'.format(os.getpid()))
    p = Process(target=run_proc, args=(1,))
    p.start()
    p.join()


class Test_02(Process):  # 继承版
    def __init__(self, num):
        super().__init__()
        self.num = num

    def run(self) -> None:
        run_proc(self.num)


def test_03():
    """池化"""
    print('当前进程号: {}'.format(os.getpid()))
    pool = Pool()
    for _ in range(5):
        pool.apply_async(run_proc, args=(1,))
    pool.close()  # 关闭进程池，阻止更多的任务提交到进程池Pool，待任务完成后，工作进程会退出
    # p.terminate()：结束工作进程，不再处理未完成的任务

    pool.join()  # 等待工作线程的退出，必须在close()或terminate()之后使用，
    # 因被终止的进程需要被父进程调用wait（join等价于wait）,否则进程会成为僵尸进程。


def test_04():
    """map 方法"""
    print('当前进程号: {}'.format(os.getpid()))
    pool = Pool()
    pool.map(run_proc, [1 for _ in range(5)])
    pool.close()  # 关闭进程池，阻止更多的任务提交到进程池Pool，待任务完成后，工作进程会退出
    # p.terminate()：结束工作进程，不再处理未完成的任务

    pool.join()  # 等待工作线程的退出，必须在close()或terminate()之后使用，
    # 因被终止的进程需要被父进程调用wait（join等价于wait）,否则进程会成为僵尸进程。


if __name__ == '__main__':
    test_01()
    print('--------------------------------分隔线---------------------------')
    t1 = Test_02(1)
    t1.start()
    t1.join()
    print('--------------------------------分隔线---------------------------')
    test_03()
    print('--------------------------------分隔线---------------------------')
    test_04()
