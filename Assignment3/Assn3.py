# -*- coding: utf-8 -*-
"""
Created on Sat May 23 22:28:34 2020
"""

# Discussion in video
# https://youtu.be/j_hV_LsxLqA

"""
Referance:
GMM of EM
https://www.youtube.com/watch?v=kkAirywakmk
"""

import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt


img = cv.imread('firstImage.jpg')
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)

cv.imwrite('gray.jpg',gray)
plt.imshow(gray, cmap = "gray"),plt.show()


# play with openCV
color = ('b','g','r')
for i,col in enumerate(color):
    histr = cv.calcHist([img],[i],None,[256],[0,256])
    plt.plot(histr,color = col)
    plt.xlim([0,256])
plt.show()

plt.hist(gray.ravel(),256,[0,256]); plt.show()

# define gaussion function

def Gaussion(x, mu, sigma):
    g = (1/(sigma*np.sqrt(2*np.pi)))*np.exp(-0.5 * ((x-mu)/sigma)**2)
    return g;

for x in range(0, 255):
    #print(x, Gaussion(x, 127, 30))
    plt.plot(x, Gaussion(x, 127, 30), '.b')
    plt.plot(x, Gaussion(x, 50, 20), '.g')
plt.show()

# using gray image from now on

# histogram
histogram, bin_edges = np.histogram(gray, bins = 255, range = (0, 255))
plt.figure() 
plt.title("Grayscale Histogram")
plt.xlabel("grayscale value")
plt.ylabel("pixels")
plt.xlim([0, 255])
plt.plot(bin_edges[0:255], histogram)

plt.show()

# histogram
histogram, bin_edges = np.histogram(gray, bins = 255, range = (0, 255), density = True)
plt.figure() 
plt.title("Grayscale Histogram")
plt.xlabel("grayscale value")
plt.ylabel("probability")
plt.xlim([0, 255])
plt.plot(bin_edges[0:255], histogram)

plt.show()
#histogram with gaussion value
plt.figure() 
plt.title("Grayscale Histogram with Gaussian")
plt.xlabel("grayscale value")
plt.ylabel("probability")
plt.xlim([0, 255])
plt.plot(bin_edges[0:255], histogram)
for x in range(0, 256):
    #print(x, Gaussion(x, 100, 20))
    plt.plot(x, 0.2 * Gaussion(x, 115, 10), '.b')
    plt.plot(x, 0.8 * Gaussion(x, 40, 20), '.g')
plt.show()

#histogram with combined gausion
plt.figure() 
plt.title("Grayscale Histogram")
plt.xlabel("grayscale value")
plt.ylabel("pixels")
plt.xlim([0, 255])
plt.plot(bin_edges[0:255], histogram)
for x in range(0, 256):
    #print(x, Gaussion(x, 100, 20))
    plt.plot(x, 0.2 * Gaussion(x, 115, 10) + 0.8 * Gaussion(x, 40, 20), '.b')
    
plt.show()

# using library
from sklearn.mixture import GaussianMixture as GMM

gray2 = gray.reshape((-1,1))
gmm_model = GMM(n_components = 2, covariance_type = 'tied').fit(gray2)

gmm_labels = gmm_model.predict(gray2)

original_shape = img.shape
segmented = gmm_labels.reshape(original_shape[0], original_shape[1])
segmented[segmented == 1] = 255
plt.imshow(segmented, cmap = "gray"),plt.show()
cv.imwrite("segmented_plant_gray.jpg", segmented)