"""
@author: yrmt
@contact: butanoler@gmail.com
@file: d_class_05_私有化.py
@time: 2019/8/18
"""


# 约定: https://www.python.org/dev/peps/pep-0008/

class A(object):
    __code = 'python'  # 私有 类属性 存在于 类对象dict中 _A__code
    _code = 'python'  # 类属性 存在于 类对象dict中 _code
    code = 'python'  # 类属性 存在于 类对象dict中 code

    def __init__(self):
        self.__name = 'butanoler'  # 私有属性 存在于实例对象dict内_A__name
        self._name = 'butanoler'  # 存在于实例对象dict内 _name
        self.name = 'butanoler'  # 存在于实例对象dict内 name

    def __aa(self):
        # 私有属性只是更改dict中名字 _A__aa
        print("this is A.__aa")

    def aa(self):
        # 公共属性应该没有前导下划线。
        print("this is A.aa")

    def _aa(self):
        # 如果公共属性名称与保留关键字冲突，请在属性名称后附加单个尾随下划线。
        # 这比缩写或损坏的拼写更可取。
        print("this is A._aa")


a = A()
print(A.__dict__)  # 类对象属性
print(a.__dict__)  # 实例对象属性
print(dir(A))  # A.__dict__ 是dir(A)的子集
print(dir(a))  # a.__dict__ 是dir(a)的子集
a._aa()
a._A__aa()  # 尽量不要这样使用
print(A._A__code)
print(a._A__name)
print('--------------------------------分隔线---------------------------')


class B(A):
    def __init__(self):
        super().__init__()


b = B()
# 每个类有自己的__dict__属性，就算存着继承关系，父类的__dict__ 并不会影响子类的__dict__
print(B.__dict__)  # 类对象属性
# 对象也有自己的__dict__属性，父子类对象公用__dict__
print(b.__dict__)  # 实例对象属性
print(dir(B))  # __dict__是dir()的子集 , 还会扫父类的类属性
print(dir(b))  # __dict__是dir()的子集 , 还会扫父类的实例属性
b._aa()
b._A__aa()
print(B._A__code)
print(b._A__name)
