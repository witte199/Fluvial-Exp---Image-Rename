# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import glob
import numpy as np
import os

# Directory with photos
cwd = r'E:\151124_MC_DW_IW_01\photoTest'

os.chdir(cwd)
photos = glob.glob('*.jpg')

newphotos = photos[:]
for i in range(len(newphotos)):
    t = i*20
    #newphotos[i] = newphotos[i].replace('Img', 'xxx')
    newphotos[i] = 'img_'+ ('%06d' %t) + '.jpg'

for i in range(len(newphotos)):
    os.rename(photos[i], newphotos[i])