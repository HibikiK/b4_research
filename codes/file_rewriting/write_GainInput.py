import numpy as np
import h5py
import os

if os.path.exists('output.dat'):
    print('Organizing gain input Data')
    os.remove('output.dat')
else:
    print('Organizing gain input Data')

# EzOutputの取得
f = h5py.File('gprMax.out', 'r')
f_dataset = f['/rxs/rx1/Ez']
arr = f_dataset[...]
size = len(arr)

f.close

# Time_Windowの取得
TimeStep = 60/12721

print(TimeStep)
print(size)

# 出力ファイルの作成、
# ファイルへの書き込み
tf = open('output.dat', mode='w')

L = []
for i in range(size):
    time = str("{0:<8.8f}".format(i*TimeStep))
    Ez = str("{0:<8.8f}".format(f_dataset[i]))
    L.append(time)
    L.append('  ')
    L.append(Ez)
    L.append('\n')
    s = ''.join(L)

tf.write(s)
tf.close

print('gprEz Data Coppied as gain input file as "output.dat"')
