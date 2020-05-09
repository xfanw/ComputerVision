# -*- coding: utf-8 -*-
"""
Spyder Editor
Harris
This is a temporary script file.
"""
import numpy as np
import cv2 as cv
img = cv.imread('firstImage.jpg')
img2 = cv.imread('secondImage.jpg')
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
gray2 = cv.cvtColor(img2,cv.COLOR_BGR2GRAY)

#Create SIFT
sift = cv.xfeatures2d.SIFT_create()

kp = sift.detect(gray,None)
img = cv.drawKeypoints(img,kp,img)

kp2 = sift.detect(gray2,None)
img2 = cv.drawKeypoints(img2,kp2,img2)

#img=cv.drawKeypoints(gray,kp,img,flags=cv.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
#Draw Img
cv.imwrite('sift_keypoints_first.jpg',img)
cv.imwrite('sift_keypoints_second.jpg',img2)