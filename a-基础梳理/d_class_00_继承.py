"""
@author: yrmt
@contact: butanoler@gmail.com
@file: d_class_00_继承.py
@time: 2019/8/15
"""


# dry原则:
# Don't repeat yourself -> https://en.wikipedia.org/wiki/Don%27t_repeat_yourself

# 多重继承建议:
# 优先组合模式而不是继承模式。为用户提供聚合类

class A(object):
    def __init__(self):
        print('A')

    def deal(self):
        print("A.deal")


class B(A):
    def __init__(self):
        super().__init__()
        print('B')

    def deal(self):
        print("B.deal")


class C(A):
    def __init__(self):
        super().__init__()
        print('C')

    def deal(self):
        print("C.deal")


class D(B, C):
    def __init__(self):
        super().__init__()
        print('D')


print('--------------------------------分隔线---------------------------')
# 经典类和新式类:
# python2 由任意内置类型派生出的类都属于新式类，反之则为经典类。
# python3 不再区分新式类和经典类，所有的类都派生自内置类型object，都是新式类。
# 经典类多继承属性搜索顺序: 采用深度优先，先深入继承树左侧，再返回，开始找右侧
# 新式类多继承属性搜索顺序: 采用c3算法，广度优先，先水平搜索，然后再向上移动
print(D.__mro__)  # D, B, C, A

# 继承图
#       A
#     ↙ ↘
#    B    C
#    ↘  ↙
#       D
d = D()
d.deal()
