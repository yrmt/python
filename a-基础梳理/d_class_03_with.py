"""
@author: yrmt
@contact: butanoler@gmail.com
@file: d_class_03_with.py
@time: 2019/8/17
"""
# with : 上下文管理器
# https://www.python.org/dev/peps/pep-0343/
# https://stackoverflow.com/questions/3012488/what-is-the-python-with-statement-designed-for

from contextlib import contextmanager


@contextmanager
def working(path):  # 像极了闭包
    print("do something before: {}".format(path))
    li = ['a', 'b']
    try:
        yield li
    finally:
        print("do something after")


with working("/aaa/bbb/ccc") as lii:
    print("lii :{}".format(lii))
print('--------------------------------分隔线---------------------------')


class Working(object):
    def __enter__(self):
        print("__enter__")
        return ['a', 'b']

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("__exit__", exc_type, exc_val, exc_tb)


with Working() as w:
    print(w)
    # raise Exception('异常?')
print('--------------------------------分隔线---------------------------')


class AsyncContextManager:
    # https://www.python.org/dev/peps/pep-0492/
    async def log(self, context):
        print(context)

    async def __aenter__(self):
        await self.log('entering context')
        return ['1', '2', '3']

    async def __aexit__(self, exc_type, exc, tb):
        await self.log('exiting context')

# async with AsyncContextManager() as am:
#     pass
