import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt

# 版本检查
print(mpl.__version__)  # > 3.0.0


# 导入数据集
midwest = pd.read_csv(
    "https://raw.githubusercontent.com/selva86/datasets/master/midwest_filter.csv")


# midwest['category']分类，颜色设置为与其一样多
categories = np.unique(midwest['category'])
colors = [plt.cm.tab10(i/float(len(categories)-1))
          for i in range(len(categories))]

# 每个分类plot
plt.figure(figsize=(16, 10), dpi=80, facecolor='w', edgecolor='k')

for i, category in enumerate(categories):
    plt.scatter('area', 'poptotal',
                data=midwest.loc[midwest.category == category, :],
                s=20, c=colors[i], label=str(category))

# 修改x轴,y轴坐标系尺寸区间
plt.gca().set(xlim=(0.0, 0.1), ylim=(0, 90000),
              xlabel='Area', ylabel='Population')

plt.xticks(fontsize=12)
plt.yticks(fontsize=12)
plt.title("Midwest Area vs Population", fontsize=22)
plt.legend(fontsize=12)
plt.show()
