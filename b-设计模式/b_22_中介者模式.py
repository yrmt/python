# User类统一接口，User1和User2分别是不同的对象，二者之间有关联，
# 如果不采用中介者模式，则需要二者相互持有引用，这样二者的耦合度很高，
# 为了解耦，引入了Mediator类，提供统一接口，MyMediator为其实现类，
# 里面持有User1和User2的实例，用来实现对User1和User2的控制。
# 这样User1和User2两个对象相互独立，他们只需要保持好和Mediator之间的关系就行，
# 剩下的全由MyMediator类来维护！
class User(object):
    def __init__(self, media):
        self.media = media


class User1(User):
    def work(self):
        print("User1 work", self.media.name)


class User2(User):
    def work(self):
        print("User2 work", self.media.name)


class Mediator(object):
    def __init__(self, name):
        self.users = list()
        self.name = name

    def createMediator(self):
        self.users.append(User1(self))
        self.users.append(User2(self))

    def workAll(self):
        for user in self.users:
            user.work()


m = Mediator("mediator 01")
m.createMediator()
m.workAll()
