import numpy as np
import h5py
import os


if os.path.exists('EzOutput.out'):
    print('Aquiring gprEz Data')
    os.remove('EzOutput.out')
else:
    print('Aquiring gprEz Data')


# 出力ファイルオープン
# Ez出力結果の取得
f2 = h5py.File('gprMax.out', 'r')
f_dataset = f2['/rxs/rx1/Ez']
arr = f_dataset[...]
size = len(arr)

f2.close


tf = open('EzOutput.out', mode='w')

for i in range(size):
    s = str(f_dataset[i])
    tf.write(s + '\n')

tf.close

print('gprEz Data Written in "EzOutput.out"')
