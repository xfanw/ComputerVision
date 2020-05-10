# -*- coding: utf-8 -*-
"""
Created on Sun May 10 13:21:54 2020

@author: Administrator
"""
import numpy as np
objp = np.zeros((1, 24, 3), np.int)
print(objp)
objp[0,:,:2] = np.mgrid[0:8, 0:3].T.reshape(-1, 2)

print(objp)