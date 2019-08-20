"""
@author: yrmt
@contact: butanoler@gmail.com
@file: d_class_iter.py
@time: 2019/8/15
"""


# for/else -> http://book.pythontips.com/en/latest/for_-_else.html

# 迭代器
class IterClass(object):
    def __init__(self):
        self.names = ['a01', 'a02', 'b01', 'c01', 'c03']
        self.index = 0

    def __iter__(self):
        print("__iter__")
        self.index = 0
        return self

    def __next__(self):
        print("__next__")
        if len(self.names) > self.index:
            name = self.names[self.index]
            self.index += 1
            return name
        else:  # 扔出StopIteration 会停止迭代
            raise StopIteration


it = iter(IterClass())
print(it)
print(next(it))
print('--------------------------------分隔线---------------------------')

ic = IterClass()
for name in ic:
    print(name)
else:  # 如果没有遇到break 则输出
    print("end iter and no break")
print('--------------------------------分隔线---------------------------')

for name in ic:
    if name == 'a01':
        break
    print(name)
else:
    print("end iter and no break")
