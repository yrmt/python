import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

moneys = pd.read_csv("a_03_matplotlib_food.csv")

fig = plt.figure(figsize=(6, 6))

ax1 = fig.add_subplot(4, 4, 1)  # 4,4矩阵大小 1 对应位置
ax2 = fig.add_subplot(4, 4, 2)
aa2 = fig.add_subplot(2, 2, 2)
ab1 = fig.add_subplot(4, 2, 3)

a43 = fig.add_subplot(2, 2, 3)

ax1.plot(moneys['year'], moneys['money'])  # 画对象
ax1.set_xticks(np.arange(0, 16, 8) + 2000)
ax1.set_xlabel('year')
ax1.set_ylabel('money')
ax1.set_title('fuck you')
for xt in ax1.get_xticklabels():
    xt.set_rotation(90)
# plt.xticks(rotation=90)  # 如果不是共用轴，就可以设置。现在共用X轴就无法使用xticks的rotation来对x周标签旋转

aa2.plot(np.random.randint(1, 100, 30), np.arange(30), c='blue', label='aa')
aa2.plot(np.random.randint(1, 100, 30), np.arange(30), c='red', label='bb')
aa2.plot(np.random.randint(1, 100, 30), np.arange(30), c='orange', label='cc')
aa2.legend(loc='best')

ab1.bar([1, 2, 3, 4], [4, 5, 6, 7], 0.5)  # 1234 x轴 ，4567 y轴 ， 0.5列宽

a43.scatter(np.arange(0, 50), np.random.random(50)*np.arange(0, 50))

plt.show()
