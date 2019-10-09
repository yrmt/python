class Memento(object):
    def __init__(self, value):
        self.value = value


class Original(object):
    def __init__(self, _value):
        self._value = _value

    def createMenmento(self):
        return Memento(self._value)

    def restoreMemento(self, memento):
        self._value = memento.value


if __name__ == '__main__':
    o = Original("tmp01")
    m = o.createMenmento()
    o._value = 'tmp01_change'
    print(o._value)
    o.restoreMemento(m)
    print(o._value)
