# 聚类算法
# K_MEANS 算法
#   需要指定K值，表示有几个类。
#   质心： 均值，即向量各维平均值即可
#   距离的度量：常用欧几里得距离和余弦相似度
#   优点： 比较简单，快速适合常规数据集
#   缺点： k难以确定，复杂度与样本呈线性关系，很难发现任意形状的簇
from sklearn.cluster import KMeans

# DBSCAN (Density-Based Spatial Clustering of Applications with Noise) 基于密度带有噪声点的（发展下线算法）
# 核心对象：若某个点的密度达到算法设定的阈值则其位核心点
# 领域的距离阈值： 设定的半径r（可以根据k距离来设定，找突变点）
# 直接密度可达：若某个点p在点q的r领域内，且q是核心点p-q直接密度可达
# 密度可达：若有一个点的序列q0,q1,...qk , 对任意qi-qi-1是直接密度可达的，则称从q0到qk密度可达，这实际上是直接密度可达的传播
# 可用于 异常检测
# 优点：不需要指定簇个数，可以发现任意形状的簇，擅长找到离群点，两个参数就够了
# 缺点：高纬数据有些困难（可以降维），参数难以选择，sklearn效率很慢（数据消减策略）。

# BIRCH 聚类算法(速度最快)
# MEAN_SHIFT

# 聚类评估（轮廓系数（Silhouette Coefficient））：
# 同簇内越小越好，异簇内越大越好。
from sklearn import metrics
