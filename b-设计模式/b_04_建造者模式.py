# （生成器模式）适用场景，优点：
#   多个功能组合为一个产品，
#   不必关心产品细节
# 汽车 ： 轮子，档位，发动机


class Wheels(object):
    def run(self):
        print("wheels run")

    def stop(self):
        print("wheels stop")


class Gears(object):
    def run(self):
        print("Gears run")

    def stop(self):
        print("gears stop")


class Engines(object):
    def run(self):
        print("Engines run")

    def stop(self):
        print("engines stop")


class Bus(object):
    def __init__(self):
        self.e = Engines()
        self.g = Gears()
        self.w = Wheels()

    def run(self):
        self.e.run()
        self.g.run()
        self.w.run()
        print("bus run ")
        self.w.run()
        self.g.run()
        self.e.run()


if __name__ == '__main__':
    b = Bus()
    b.run()
