import h5py
import os
import numpy as np
import pandas as pd
from pandas import Series, DataFrame
import matplotlib.pyplot as plt
import seaborn as sns
import linecache


filepath1 = 'heatmap.png'
if os.path.exists(filepath1):
    print('Aquiring gpr Scan Data')
    os.remove(filepath1)
else:
    print('Aquiring gpr Scan Data')

# スキャンデータの取得
filepath2 = '20191209COG_data.txt'


# 全行数の取得
TotalLines = sum([1 for _ in open(filepath2)])

# 全列数の取得
TotalColumns = len(linecache.getline(filepath2, 1).strip().split())
# Traceは0~46の47個


x = 1
# 振幅データの取得


amplitude = []
for a in range(1, TotalLines):
    timePoint = linecache.getline(filepath2, a).strip().split()
    ampRow = []
    for b in range(TotalColumns):
        ampRow.append(float(timePoint[b]))
    amplitude.append(ampRow)


# Traceは0~46の47個


# ヒートマップの描画
sns.heatmap(amplitude, cmap="Reds")
plt.show()
