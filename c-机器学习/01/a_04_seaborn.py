import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import matplotlib as mpl

# sns.set_style("whitegrid")
# sns.set_style("dark")
# data = np.random.normal(size=(20, 6)) + np.arange(6) / 2
# sns.boxplot(data=data)
# sns.despine(offset=4,)

with sns.axes_style('darkgrid'):
    plt.subplot(211)
plt.subplot(212)
plt.show()
