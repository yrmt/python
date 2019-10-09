# 访问者模式就是一种分离对象数据结构与行为的方法，
# 通过这种分离，可达到为一个被访问者动态添加新的操作而无需做其它的修改的效果


class Visitor(object):
    def visit(self, sub):
        print("visit the subject ", sub.get_subject())


class Subject(object):
    def accept(self, visitor):
        visitor.visit(self)

    def get_subject(self):
        return "love"


v = Visitor()
s = Subject()
s.accept(v)
