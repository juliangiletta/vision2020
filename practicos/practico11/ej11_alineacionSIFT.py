import numpy as np
import cv2

MIN_MATCH_COUNT = 10

img1 = cv2.imread('img1.jpg')   # Leemos la imagen 1
img2 = cv2.imread('img2.jpg')   # Leemos la imagen 2

cp_img1 = img1.copy()
cp_img1 = img2.copy()

dscr = cv2.xfeatures2d.SIFT_create()

kp1, des1 = dscr.detectAndCompute(img1, None)
kp2, des2 = dscr.detectAndCompute(img2, None)

cv2.drawKeypoints(cp_img1, kp1, cp_img1)
cv2.drawKeypoints(cp_img2, kp2, cp_img2,) 

cv2.imshow('sift_keypoints', cp_img1)
cv2.waitKey(0)
cv2.imshow('sift_keypoints', cp_img2)
cv2.waitKey(0)

#matcher = cv2.BFMatcher(cv2.NORM_L2)

#matches = matcher.knnMatch(des1, des2, k=2)
