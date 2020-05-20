import numpy as np
import pandas as pd

data = pd.read_csv('a_02_pandas_food.csv')
# print(help(pd.read_csv))
print(data)
print("*" * 10)
print(data.head(2))
print("*" * 10)
print(data.tail(1))
print("*" * 10)
print(data.columns)
print("*" * 10)
print(data.loc[[0, 2]])  # 取第一行数据
print(data.loc[1:2])  # 取第一行数据
print("*" * 10)
print(data['name'])
print("*" * 10)
print(data[['name', 'age']])
# 16 已完成
print("*" * 10)

print(data.sort_values("age"))  # 排序 inplace是否替换，ascending顺序


# data.pivot_table(index="name", values="Survived", aggfunc=np.mean)  # 补全
# data.dropna(axis=0, subset=['age'])  # 删除 列为空的
# data.reset_index(drop=True)  # 排序后重置索引


def hundlerdth_row(column):
    return column[99]


# data.apply(hundlerdth_row)  # 执行对应函数
def age_lable(row):
    age = row['age']
    if age > 22:
        return '22以上'
    else:
        return '22一下'


print(data.apply(age_lable, axis=1))  # 执行对应函数
