import numpy
import numpy as np

v1 = numpy.asarray([5, 10, 15, 20])
eq = ((v1 == 5) & (v1 == 10))
eq = ((v1 == 5) | (v1 == 10))
print(eq)
print(v1.dtype)
v1 = v1.astype(float)
print(v1.dtype)
v2 = numpy.asarray([
    [1, 2, 3, 4],
    [2, 3, 4, 5],
    [3, 4, 5, 6]
])
print(v2.sum(axis=1))
print(v2.sum(axis=0))

v3 = numpy.arange(15)
print(v3.reshape(3, 5))

print(numpy.zeros((3, 5)))
print(numpy.ones((3, 5), dtype=int))
print(numpy.arange(3, 30, 3))
print("*" * 10)
print(np.random.random((2, 3)))
print("*" * 10)
print(np.linspace(0, 10, 100, dtype=int))
print(np.linspace(0, 10, 100, dtype=int) ** 2)
print(np.linspace(0, 10, 100, dtype=int) < 5)
print("*" * 10)
a = np.array([[1, 1], [0, 1]])
b = np.array([[2, 0], [3, 4]])
print(a * b)  # 对应位置相乘
print(a.dot(b))
print(np.dot(a, b))
print(a.ravel())

c = np.arange(20)
print(c.reshape(-1, 5))
print(c.reshape(-1, 4))
print("*" * 10)
d = np.arange(10, 30, 2).reshape((-1, 2))
e = np.arange(30, 50, 2).reshape((-1, 2))
print(d)
print(e)
print(np.hstack((d, e)))  # 横向拼接
print(np.vstack((d, e)))  # 竖向拼接
print("*" * 10)
f = np.floor(10 * np.random.random((4, 4)))
print(f)
print(np.hsplit(f, 4))  # 横切成固定的四份
print(np.vsplit(f, 4))  # 竖切固定四份
print(np.vsplit(f, (1, 3,)))  # 竖切指定的份
print("*" * 10)
print(np.tile(np.arange(4), (2, 3)))
