import sys
import cv2 as cv
import numpy as np
img_orig = cv.imread("1.jpg")
# 灰度化
img_gray = cv.cvtColor(img_orig, cv.COLOR_BGR2GRAY)
# 中值滤波
blur = cv.GaussianBlur(img_gray, (5, 5), 0)
# 二值化
ret, thre = cv.threshold(img_gray, 180, 255, cv.THRESH_TRIANGLE + cv.THRESH_BINARY_INV)
# 腐蚀
# 提取轮廓
contours, hierarchy = cv.findContours(thre, cv.RETR_TREE, cv.CHAIN_APPROX_NONE)
contours_r = []
for i, contour in enumerate(contours):
    ar = cv.contourArea(contours[i])  # 计算面积
    if ar > 50:
        num, _, _ = contour.shape
        for i in range(num):
            if i == 0:
                contours_r.append("M " + str(contour[i][0][0]) + "," + str(contour[i][0][1]))
            contours_r.append("L " + str(contour[i][0][0]) + "," + str(contour[i][0][1]))
filename = open("4.txt", "w")
filename.write("#000000\nW482H256\n")
for value in contours_r:
    filename.write(str(value) + "\n")
    print(value)
filename.close()
