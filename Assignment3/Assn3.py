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
plt.imshow(gray, cmap = "gray"),plt.show()


# play with openCV
"""
color = ('b','g','r')
for i,col in enumerate(color):
    histr = cv.calcHist([img],[i],None,[256],[0,256])
    plt.plot(histr,color = col)
    plt.xlim([0,256])
plt.show()
"""
# define gaussion function

def Gaussion(x, mu, sigma):
    g = (1/(sigma*np.sqrt(2*np.pi)))*np.exp(-0.5 * ((x-mu)/sigma)**2)
    return g;

# using gray image from now on

plt.hist(gray.ravel(),256,[0,256]); plt.show()

# histogram
histogram, bin_edges = np.histogram(gray, bins = 255, range = (0, 255), density = True)
plt.figure() 
plt.title("Grayscale Histogram")
plt.xlabel("grayscale value")
plt.ylabel("pixels")
plt.xlim([0, 255])
plt.plot(bin_edges[0:255], histogram)

plt.show()

#histogram with gaussion value
plt.figure() 
plt.title("Grayscale Histogram")
plt.xlabel("grayscale value")
plt.ylabel("pixels")
plt.xlim([0, 255])
plt.plot(bin_edges[0:255], histogram)
for x in range(0, 256):
    #print(x, Gaussion(x, 100, 20))
    plt.plot(x, 0.2 * Gaussion(x, 115, 10), '.b')
    plt.plot(x, 0.8 * Gaussion(x, 40, 20), '.g')
plt.show()

plt.figure() 
plt.title("Grayscale Histogram")
plt.xlabel("grayscale value")
plt.ylabel("pixels")
plt.xlim([0, 255])
plt.plot(bin_edges[0:255], histogram)
for x in range(0, 256):
    #print(x, Gaussion(x, 100, 20))
    plt.plot(x, 0.2 * Gaussion(x, 115, 10), '.b')
    plt.plot(x, 0.8 * Gaussion(x, 40, 20), '.g')
plt.show()
''' TEST
for x in range(0, 255):
    print(x, Gaussion(x, 100, 20))
    plt.plot(x, Gaussion(x, 100, 20), '.b')
plt.show()
'''
gray[gray<120] = 0
gray[gray>120] = 255
plt.imshow(gray, cmap = "gray"),plt.show()

