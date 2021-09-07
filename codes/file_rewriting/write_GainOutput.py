import numpy as np
import h5py
import os

# Time_Windowの取得
TimeStep = 60/12721

# datファイルオープン
filepath2 = './gain_output.dat'

with open(filepath2) as f2:
    lines = f2.readlines()
    lines_strip = [line.strip() for line in lines]

# 最終行の取得
TotalLines = len(lines)
f2.close

# ファイル作成
filepath3 = 'gainedEz.out'
if os.path.exists(filepath3):
    print('Aquiring and Writing Gained Ez Data')
    os.remove(filepath3)
else:
    print('Aquiring and Writing Gained Ez Data')

# 出力ファイルの作成、
# ファイルへの書き込み
tf = open('gainedEz.out', mode='w')

X = []
for i in range(1, TotalLines):
    time = str("{0:<8.8f}".format((i-1)*TimeStep))
    amplitude = lines_strip[i].split()
    X.append(time)
    X.append(' ')
    X.append(amplitude[1])
    X.append('\n')
    s = ''.join(X)

tf.write(s)

print('gprEz Output(Gained) is Written in "gainedEz.xlsx"')
