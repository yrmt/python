# 模型保存
# from sklearn.externals import joblib
import joblib
from sklearn import svm

x = [[0, 0], [1, 1]]
y = [0, 1]
clf = svm.SVC()
clf.fit(x, y)
joblib.dump(clf, "model_svm_dump.m")
# clf = joblib.load("train_model.m")
# clf.fit(test_X)
