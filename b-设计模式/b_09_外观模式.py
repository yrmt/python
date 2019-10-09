# 避免互相持有实例，各个模块之间解耦


class CPU(object):
    def start(self):
        print("cpu start")

    def shutdown(self):
        print("CPU shutdown")


class Memory(object):
    def start(self):
        print("Memory start")

    def shutdown(self):
        print("Memory shutdown")


class Disk(object):
    def start(self):
        print("Disk start")

    def shutdown(self):
        print("Disk shutdown")


class Computer(object):
    def __init__(self):
        self.c = CPU()
        self.m = Memory()
        self.d = Disk()

    def start(self):
        self.c.start()
        self.m.start()
        self.d.start()

    def shutdown(self):
        self.c.shutdown()
        self.m.shutdown()
        self.d.shutdown()


if __name__ == '__main__':
    c = Computer()
    c.start()
    c.shutdown()
