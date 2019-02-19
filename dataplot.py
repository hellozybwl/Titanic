# -*- coding: utf-8 -*-
import matplotlib as mpl
mpl.use('TkAgg')

import pandas as pd #数据分析
import numpy as np #科学计算
from pandas import Series,DataFrame
from sklearn.ensemble import RandomForestRegressor

data_train = pd.read_csv("Train.csv")

import matplotlib.pyplot as plt
fig = plt.figure()
fig.set(alpha=0.2)  # 设定图表颜色alpha参数

#plt.subplot2grid((2,3),(0,0))             # 在一张大图里分列几个小图


# Survived_0 = data_train.Parch[data_train.Survived == 0].value_counts()
# Survived_1 = data_train.Parch[data_train.Survived == 1].value_counts()
# df=pd.DataFrame({u'0':Survived_0, u'1':Survived_1})
# df.plot(kind='bar', stacked=True)

print(data_train[data_train['Name'].str.contains("Major")])

print(data_train[data_train['Name'].str.contains("Mrs")][data_train['Parch'] < 4])



#plt.show()