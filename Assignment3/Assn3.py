# -*- coding: utf-8 -*-
"""
Created on Sat May 23 22:28:34 2020

@author: Administrator
"""

import pandas as pd
import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt


img = cv.imread('firstImage.jpg')
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)

cv.imwrite('gray.jpg',gray)