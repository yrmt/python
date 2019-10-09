# 迭代器
class Iterator(object):
    def __init__(self, collection):
        self.names = collection
        self.index = 0

    def __iter__(self):
        self.index = 0
        return self

    def __next__(self):
        if len(self.names) > self.index:
            name = self.names[self.index]
            self.index += 1
            return name
        else:  # 扔出StopIteration 会停止迭代
            raise StopIteration


class Collection(list):
    def iterator(self):
        return Iterator(self)

    def get(self, i):
        return self[i]

    def size(self):
        return len(self)


c = Collection()
c.append("sadf1")
c.append("sadf2")
c.append("sadf3")
print(c.size())
print(c.get(1))
print("*" * 30)
for it in c.iterator():
    print(it)
