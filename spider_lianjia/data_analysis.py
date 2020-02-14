import matplotlib
import pandas as pd
import xlrd
import numpy as np
import seaborn as sns
import matplotlib as mpl
import matplotlib.pyplot as plt
from IPython.display import display
plt.style.use("fivethirtyeight")
sns.set_style({'font.sans-serif': ['simhei', 'Arial']})
# %matplotlib inline

lianjia_df = pd.read_csv('lj.csv', encoding='GBK')
display(lianjia_df.head(n=2))

# lianjia_df.info()
lianjia_df.describe()


# df = lianjia_df.copy()

# 重新摆放列位置
# Type, Floor, Area, Structure, Inarea, Architectural_type, Orientation, Building_structure, Situation, Ratio, Elevator, Years, Price, PerPrice, Region, No
# columns = ['Type', 'Floor', 'Area', 'Structure', 'Inarea', 'Architectural_type', 'Orientation', 'Building_structure', 'Situation', 'Ratio', 'Elevator', 'Years', 'Price', 'PerPrice', 'Region', 'No']
# df = pd.DataFrame(lianjia_df, columns=columns)

# 重新审视数据集
display(lianjia_df.head(n=2))
# 对二手房区域分组对比二手房数量和每平米房价
df_house_count = lianjia_df.groupby('Region')['Price'].count().sort_values(ascending=False).to_frame().reset_index()
print(df_house_count)
df_house_mean = lianjia_df.groupby('Region')['PerPrice'].mean().sort_values(ascending=False).to_frame().reset_index()

# f, ax1 = plt.subplots(1, 1, figsize=(10, 5))
# sns.barplot(x='Region', y='PerPrice', palette="Blues_d", data=df_house_mean, ax=ax1)
# ax1.set_title('兰州各大区二手房每平米单价对比', fontsize=15)
# ax1.set_xlabel('区域')
# ax1.set_ylabel('每平米单价')

f, [ax1, ax2, ax3] = plt.subplots(1, 3, figsize=(30, 20))
sns.barplot(x='Region', y='PerPrice', palette="Blues_d", data=df_house_mean, ax=ax1)
ax1.set_title('兰州各大区二手房每平米单价对比', fontsize=15)
ax1.set_xlabel('区域')
ax1.set_ylabel('每平米单价')

sns.barplot(x='Region', y='Price', palette="Greens_d", data=df_house_count, ax=ax2)
ax2.set_title('兰州各大区二手房数量对比', fontsize=15)
ax2.set_xlabel('区域')
ax2.set_ylabel('数量')

sns.boxplot(x='Region', y='Price', data=lianjia_df, ax=ax3)
ax3.set_title('兰州各大区二手房房屋总价', fontsize=15)
ax3.set_xlabel('区域')
ax3.set_ylabel('房屋总价')

plt.show()

f, [ax1, ax2] = plt.subplots(1, 2, figsize=(15, 5))
# 建房时间的分布情况
sns.distplot(lianjia_df['Area'], bins=20, ax=ax1, color='r')
sns.kdeplot(lianjia_df['Area'], shade=True, ax=ax1)
# 建房时间和出售价格的关系
sns.regplot(x='Area', y='Price', data=lianjia_df, ax=ax2)
plt.show()
