class StateFunc(object):
    def __init__(self, value):
        self.value = value

    def method_01(self):
        print("StateFunc method_01")

    def method_02(self):
        print("StateFunc method_02")


class Execute(object):
    def __init__(self, sf):
        self.sf = sf

    def method(self):
        if self.sf.value == '01':
            self.sf.method_01()
        elif self.sf.value == '02':
            self.sf.method_02()


if __name__ == '__main__':
    sf = StateFunc("01")
    e = Execute(sf)
    e.method()
    sf.value = '02'
    e.method()
