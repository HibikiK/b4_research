import shutil
import os

if os.path.exists('Gain.dat'):
    print('Executing Gain2')
    shutil.copyfile("./input_gain_ex2.par", "./input_gain.par")

else:
    print('Executing Gain1')
    shutil.copyfile("./input_gain_ex1.par", "./input_gain.par")
