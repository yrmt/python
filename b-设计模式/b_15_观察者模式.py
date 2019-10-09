import abc


class ObsInterface(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def update(self, thing):
        pass


class Obs1(ObsInterface):
    def update(self, thing):
        print("obs1 update", thing)


class Obs2(ObsInterface):
    def update(self, thing):
        print("obs2 update", thing)


class Rss(object):
    def __init__(self):
        self.obses = list()

    def add(self, obs):
        print(id(obs), "加入了")
        self.obses.append(obs)

    def delte(self, obs):
        self.obses.remove(obs)

    def notify(self):
        for obs in self.obses:
            obs.update("开饭了")


if __name__ == '__main__':
    r = Rss()
    r.add(Obs1())
    r.add(Obs2())
    r.add(Obs1())
    r.notify()
