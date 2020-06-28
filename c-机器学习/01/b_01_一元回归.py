import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# 'code', 'a', 'b',               'c', 'd', 'e', 'f', 'g'
# 000011,Y,    -792535.9688715371,0.6610273172202803,1039.473995763139,7806.432232422071,25.26865671641791,-14838

# data = pd.read_csv('analysis_2019-03-08_2019-03-22', header=None, names=['code', 'a', 'b', 'c', 'd', 'e', 'f', 'g'])
# print(data.shape)
# data_ok = data[data['g'] > 100]
# data_no = data[data['g'] <= 100]
#
# # ax = plt.subplot
# plt.scatter(data_ok['f'], data_ok['f'], s=30, c='b', marker='o', label='Adm')
# # plt.scatter(data_no['f'], data_no['f'], s=30, c='r', marker='x', label='Not')
# plt.xlabel('c')
# plt.ylabel('f')
# plt.legend()
# plt.show()
# print(data.head())
# 下采样，过采样(smote算法 模拟数据)
from imblearn.over_sampling import SMOTE

# recall 召回率 ： 1000人，990好人，10坏人，recall:0/10 评估标准
from sklearn.metrics import recall_score  # 召回率

# 80男 20女， 拿50人，20女。
#                   相关Relevant 正类                           无关non relevant负类
#   被检索到            tp(true positives)正确的判断为正确的         fp 错误判断（负例判错了）
#   未被检索到           fn(false negatives) 正类判为负               tn()负负 判断ok
# tp=20 fp=30 fn=0 tn=50

from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split  # 切分操作
# x_train,x_test,y_train,y_test = train_test_split(x, y, test_size=0.3,random_state=0)
from sklearn.model_selection import KFold, cross_val_score  # 交叉验证做几倍的。评估结果

from sklearn.linear_model import LogisticRegression  # 逻辑回归

# 正则化惩罚项
# L2 检测那个模型效果更好。

# 混淆矩阵 ！！！！

# -----------------------------决策树算法---------------------------
# 选根:
# 信息增益 gain函数 选取增益最大的
# 连续值:  贪婪算法（排序+二分）
# 过拟合:
#       预减枝： 边建立决策树边进行减枝操作（限制深度，叶子节点个数，信息增益量）
#       后减枝： 建立完成后进行减枝操作（叶子节点越多，损失越大）
# GridSearchCV 随机森林模型 自动调参
from sklearn.datasets import fetch_california_housing
from sklearn import tree

house = fetch_california_housing()
# print(house.DESCR)
# print(house.data.shape)
# print(house.data[0:10])

dtr = tree.DecisionTreeRegressor(max_depth=2)  # 构建决策树
dtr.fit(house.data[:, [6, 7]], house.target)
from sklearn.model_selection import GridSearchCV  # 网格搜索
from sklearn.ensemble import RandomForestClassifier  # 随机森林

dot_data = tree.export_graphviz(
    dtr, out_file=None, feature_names=house.feature_names[6:8],
    filled=True, impurity=False, rounded=True
)
import pydotplus

graph = pydotplus.graph_from_dot_data(dot_data)
graph.get_nodes()[7].set_fillcolor('#FFF2DD')
# from IPython.display import Image
# Image(graph.create_png())
graph.write_png("dot.png")
# ------
from sklearn.feature_selection import SelectKBest, f_classif  # 特征选择
# -----
# 归一化 -> 数据增强
# 中心化（零均值化）与标准化（归一化）

# --------------
# 标准化（归一化）两种方法：
# 1）min - max标准化（Min - MaxNormalization）
# 也称为离差标准化，是对原始数据的线性变换，使结果值映射到[0 - 1]
# 之间。转换函数如下：
# 其中max为样本数据的最大值，min为样本数据的最小值。这种方法有个缺陷就是当有新数据加入时，可能导致max和min的变化，需要重新定义。
# 2）Z - score标准化（0 - 1标准化）方法
# 这种方法给予原始数据的均值（mean）和标准差（standard
# deviation）进行数据的标准化。经过处理的数据符合标准正态分布，即均值为0，标准差为1。

