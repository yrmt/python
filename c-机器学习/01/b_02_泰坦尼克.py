import pandas

pandas.set_option('display.max_columns', None)
pandas.set_option('display.max_rows', None)
titanic = pandas.read_csv('titanic.csv')
print(titanic.describe())  # 对应每一列的 count,mean，std,min ,25%
