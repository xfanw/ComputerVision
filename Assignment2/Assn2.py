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

img_kp_sift = cv.drawKeypoints(img,kp_sift,None, flags = 4)
img2_kp_sift = cv.drawKeypoints(img2,kp2_sift,None)

cv.imwrite('out_sift_keypoints_first.jpg',img_kp_sift)
cv.imwrite('out_sift_keypoints_second.jpg',img2_kp_sift)
print("Using SIFT algorithm to find Key points: ")
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
print("Using ORB algorithm to find Key points: ")
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
cv.imwrite('out_match_20.jpg',img_out_20)
cv.imwrite('out_match_50.jpg',img_out_50)
print("Using Brute Force algorithm to find Matches: ")
plt.imshow(img_out_10),plt.show()
plt.imshow(img_out_20),plt.show()
plt.imshow(img_out_50),plt.show()

"""
    4.4: Feature Matcher Knn Match
"""

# BFMatcher with default params
bf2 = cv.BFMatcher()
matches_knn = bf2.knnMatch(des,des2, k=2)

# Apply ratio test
good = []
for m,n in matches_knn:
    if m.distance < 0.75*n.distance: #good = 135
        good.append([m])
good2 = []
for m,n in matches_knn:
    if m.distance < 0.5*n.distance: #good = 50
        good2.append([m])
good3 = []
for m,n in matches_knn:
    if m.distance < 0.2*n.distance: #good = 10
        good3.append([m])

# cv2.drawMatchesKnn expects list of lists as matches.
img_out_knn_75 = cv.drawMatchesKnn(img,kp,img2,kp2,good,None,flags=2)
img_out_knn_50 = cv.drawMatchesKnn(img,kp,img2,kp2,good2,None,flags=2)
img_out_knn_20 = cv.drawMatchesKnn(img,kp,img2,kp2,good3,None,flags=2)
cv.imwrite('out_match_Knn75.jpg',img_out_knn_75)
cv.imwrite('out_match_Knn50.jpg',img_out_knn_50)
cv.imwrite('out_match_Knn20.jpg',img_out_knn_20)
print("Using FLANN  algorithm to find Matchs: ")
plt.imshow(img_out_knn_75),plt.show()
plt.imshow(img_out_knn_50),plt.show()
plt.imshow(img_out_knn_20),plt.show()


print("PROBLEM 1: DONE!\n\nPROBLEM 2: START!")


# Define the points in first image
f1points = np.zeros((8, 2), np.int)
# Define the points in second image
f2points = np.zeros((8, 2), np.int)
i = 0

#Find matching points
for m1 in matches[:8]:
    a = (int(kp[m1.queryIdx].pt[0]), int(kp[m1.queryIdx].pt[1]))
    b = (int(kp2[m1.trainIdx].pt[0]),int(kp2[m1.trainIdx].pt[1]))

    #print("(",int(kp[m1.queryIdx].pt[0]), int(kp[m1.queryIdx].pt[1]),")\t(",int(kp2[m1.trainIdx].pt[0]),int(kp2[m1.trainIdx].pt[1]), ")")
    #print(a, b)
    f1points[i] = a
    f2points[i] = b
    i+=1

print("Coordinates in first image\n",f1points)
print("Coordinates in second image\n",f2points)

# Define the 8*8 matrix using first and second matiching key points
homoMx = np.zeros((8, 8), np.int)
result = -np.array([1,1,1,1,1,1,1,1])

#print (homoMx)
#print (result)

# calculate det of homomat
detM = np.linalg.det(homoMx)
print ("\ndetM = ", detM, "\n")
for i in range(8):
    homoMx[i] = (f1points[i][0] * f2points[i][0], f1points[i][0] * f2points[i][1], f1points[i][0], 
          f1points[i][1] * f2points[i][0], f1points[i][1] * f2points[i][1], f1points[i][1],
          f2points[i][0] , f2points[i][1])

print (homoMx, "\n")

# use equation to slove the fundamental Mx
F = np.linalg.solve(homoMx, result)
print(F, "\n")

#verify
for i in range (8):
    r = 0
    for j in range(8):
        r+= F[j]*homoMx[i][j]
    print("r== -1 ? ", r)
        
b = np.linalg.inv(homoMx)
print( b, "\n")

# use INV Mx to slove the fundamental Mx
F2 = np.zeros((8, 1))

print(F2)
for i in range(8):
    r = 0
    for j in range(8):
        r+=b[i][j]
    print(-r)
    F2[i] = -r
    
print(F2)

#verify
for i in range (8):
    r = 0
    for j in range(8):
        r+= F2[j]*homoMx[i][j]
    print("r== -1 ? ", r)
