import numpy as np
import h5py
import os
import matplotlib.pyplot as plt


if os.path.exists('EzOutput.out'):
    print('Aquiring gprEz Data')
    os.remove('EzOutput.out')
else:
    print('Aquiring gprEz Data')

if os.path.exists('EzOutput.PNG'):
    print('Drawing gprEz Graph')
    os.remove('EzOutput.PNG')
else:
    print('Drawing gprEz Graph')

# 入力ファイルオープン
# Time_Windowの取得
f1 = open('input.par', 'r')
content = f1.readlines()
num = float(content[8])
tWindow = num * 10e8

f1.close

# 出力ファイルオープン
# Ez出力結果の取得
f2 = h5py.File('gprMax.out', 'r')
f_dataset = f2['/rxs/rx1/Ez']
arr = f_dataset[...]
size = len(arr)

f2.close

# x軸リストの作成
timeStep = tWindow / size
time = [0]
for i in range(size-1):
    t = (i+1) * timeStep
    time.append(t)

# y軸リストの作成
ez = arr

# グラフ作成
fig = plt.figure(facecolor='aliceblue')
ax = fig.add_subplot(111, xlabel='Time[ns]', ylabel='Ez,Field Strength')
ax.grid(c='gainsboro', zorder=1)
ax.scatter(time, ez, color='steelblue', marker='o', s=4, zorder=5)

fig.savefig('EzOutput.png', facecolor=fig.get_facecolor())


# テキストファイルへの書き込み
tf = open('EzOutput.out', mode='w')
for i in range(size):
    s = str(f_dataset[i])
    tf.write(s + '\n')

tf.close

print('gprEz Data Written in "EzOutput.out"')
print('gprEz Graph Exported in "EzOutput.PNG')
