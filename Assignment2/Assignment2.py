# -*- coding: utf-8 -*-
"""
Spyder Editor
Harris
This is a temporary script file.
"""
import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

img = cv.imread("firstImage.jpg")
img2 = cv.imread("secondImage.jpg")

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
"""
gray = np.float32(gray)

harris = cv.cornerHarris(gray, 2, 3, 0.04)

img[harris > 0.01 * harris.max()] = [255, 0, 0]

cv.imshow("", img)

"""




sift = cv.xfeatures2d.SIFT_create()
kp = sift.detect(gray,None)
img=cv.drawKeypoints(gray,kp,img)
cv.imwrite('sift_keypoints.jpg',img)

img=cv.drawKeypoints(gray,kp,img,flags=cv.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
cv.imshow('sift_keypoints.jpg',img)