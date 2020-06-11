#coding=utf-8

import glob
import numpy as np
import cv2
import os


criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 30, 0.001)

"""
objp = np.zeros((np.prod(9*6), 3), np.float32)
objp[: , :2] = np.indices(9,6).T.reshape(-1, 2)
"""

objp = np.zeros((np.prod((8, 5)), 3), np.float32)
objp[:, :2] = np.indices((8, 5)).T.reshape(-1, 2)


objpoints = []
imgpoints = []

images = glob.glob('chess/*.png')

for fname in images:
    img = cv2.imread(fname)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    ret, corners = cv2.findChessboardCorners(gray, (8, 5), None)

    if ret is True:

        objpoints.append(objp)
        corners2 = cv2.cornerSubPix(gray, corners, (11, 11),  (-1, -1), criteria)
        imgpoints.append(corners2)

        img = cv2.drawChessboardCorners(img, (8, 5), corners2, ret)



cv2.destroyAllWindows()

ret, mtx, dist, rvecs, tvecs = cv2.calibrateCamera(objpoints, imgpoints, gray.shape[::-1], None, None)

print(mtx)

for fname in images:

    img = cv2.imread(fname)
    name = os.path.relpath(fname, 'chess')
    cv2.imwrite('chess/un_' + name, cv2.undistort(img, mtx, dist))
    
    