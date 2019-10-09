import abc


# 目标接口
class FaceUser(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def method_01(self):
        pass

    @abc.abstractmethod
    def method_02(self):
        pass


# 待适配方法
class InUser(object):
    def method_01(self):
        print("InUser method_01")


# 01. 类的适配器模式
class ClassOutUser(InUser, FaceUser):
    def method_02(self):
        print("OutUser method_02")


# 对象的适配器模式
class ObjOutUser(FaceUser):
    def __init__(self, cou):
        self.cou = cou

    def method_01(self):
        cou.method_01()

    def method_02(self):
        print("ObjOutUser method_02")


# 接口适配器模式 定义了太多接口，一些实现的时候不是都需要
class InterFaceOutUserAdp(FaceUser):
    def method_01(self):
        pass

    def method_02(self):
        pass


class InterFaceOutUser(InterFaceOutUserAdp):
    def method_01(self):
        print("InterFaceOutUser method_01")


if __name__ == '__main__':
    cou = ClassOutUser()
    cou.method_01()
    cou.method_02()
    print("*" * 100)
    oou = ObjOutUser(InUser())
    oou.method_01()
    oou.method_02()
    print("*" * 100)
    ifou = InterFaceOutUser()
    ifou.method_01()
    ifou.method_02()
