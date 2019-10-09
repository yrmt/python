class AbsHandler(object):
    def __init__(self):
        self._handler = None

    @property
    def handler(self):
        return self._handler

    @handler.setter
    def handler(self, handler):
        self._handler = handler


class MyHandler(AbsHandler):
    def __init__(self, name):
        self.name = name
        super().__init__()

    def operator(self):
        print(self.name, "deal")
        if self._handler:
            self._handler.operator()


mh1 = MyHandler('h1')
mh2 = MyHandler('h2')
mh3 = MyHandler('h3')
mh1.handler = mh2
mh2.handler = mh3
print(mh1.handler)
mh1.operator()
