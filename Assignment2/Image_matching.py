# -*- coding: utf-8 -*-
"""
Spyder Editor
Harris
This is a temporary script file.
"""
import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt
img = cv.imread('firstImage.jpg')
img2 = cv.imread('secondImage.jpg')

gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
gray2 = cv.cvtColor(img2,cv.COLOR_BGR2GRAY)

"""
    4.2 SIFT find key points
"""
#Create SIFT
sift = cv.xfeatures2d.SIFT_create()

# detect Key points of first image
kp_sift = sift.detect(gray,None)
kp_sift,des_sift = sift.compute(gray,kp_sift)
#detect key points of second image
kp2_sift = sift.detect(gray2,None)
kp2_sift,des2_sift = sift.compute(gray2,kp2_sift)

img_kp_sift = cv.drawKeypoints(img,kp_sift,None)
img2_kp_sift = cv.drawKeypoints(img2,kp2_sift,None)

cv.imwrite('out_sift_keypoints_first.jpg',img_kp_sift)
cv.imwrite('out_sift_keypoints_second.jpg',img2_kp_sift)
plt.imshow(img_kp_sift),plt.show()
plt.imshow(img2_kp_sift),plt.show()


"""
    4.2 ORB find key points
"""

# Initiate SIFT detector
orb = cv.ORB_create()

# find the keypoints and descriptors with SIFT
kp, des = orb.detectAndCompute(img,None)
kp2, des2 = orb.detectAndCompute(img2,None)

img_kp_orb = cv.drawKeypoints(img,kp,None)
img2_kp_orb = cv.drawKeypoints(img2,kp2,None)

#img=cv.drawKeypoints(gray,kp,img,flags=cv.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
#Draw Img
cv.imwrite('out_orb_keypoints_first.jpg',img_kp_orb)
cv.imwrite('out_orb_keypoints_second.jpg',img2_kp_orb)
plt.imshow(img_kp_orb),plt.show()
plt.imshow(img2_kp_orb),plt.show()

"""
    4.4: Feature Matcher
"""
# create BFMatcher object
bf = cv.BFMatcher(cv.NORM_HAMMING, crossCheck=True)

# Match descriptors.
matches = bf.match(des,des2)

# Sort them in the order of their distance.
matches = sorted(matches, key = lambda x:x.distance)

"""
    4.4 different matches
"""
# Draw first 10 matches.
img_out_10 = cv.drawMatches(img,kp,img2,kp2,matches[:10],None, flags=2)
img_out_20 = cv.drawMatches(img,kp,img2,kp2,matches[:20],None, flags=10)
img_out_50 = cv.drawMatches(img,kp,img2,kp2,matches[:50],None, flags=2)
cv.imwrite('out_match_10.jpg',img_out_10)
cv.imwrite('out_match_20.jpg',img_out_10)
cv.imwrite('out_match_50.jpg',img_out_10)

plt.imshow(img_out_10),plt.show()
plt.imshow(img_out_20),plt.show()
plt.imshow(img_out_50),plt.show()








