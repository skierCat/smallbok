# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\1.ui'
#
# Created by: PyQt5 UI code generator 5.5
#
# WARNING! All changes made in this file will be lost!
import numpy as np
import cv2
import os
from PIL import Image
from PIL import ImageEnhance

p='uint8'
o='480-640-3'
q=[]
for i in o.split('-'):
    q.append(int(i))
tmp=tuple(q)
a=np.fromfile('1月银付0001-1.bin',dtype = p)
a.shape=tmp
a=cv2.Laplacian(a,cv2.CV_64F)
cv2.imwrite('tmp.png',a)



