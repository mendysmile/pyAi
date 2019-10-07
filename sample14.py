import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

def back_projection_demo():
    sample = cv.imread("E:/image/Sample.jpg")
    target = cv.imread("E:/image/TargetImage.jpg")
    roi_hsv = cv.cvtColor(sample, cv.COLOR_BGR2HSV)
    target_hsv = cv.cvtColor(target, cv.COLOR_BGR2HSV)

    cv.imshow("sample",sample)
    cv.imshow("target",target)

    #roiHist = cv.calcHist([roi_hsv], [0, 1], None, [180, 256], [0, 180, 0, 256])
    #roiHist = cv.calcHist([roi_hsv], [0, 1], None, [36, 48], [0, 180, 0, 256])
    roiHist = cv.calcHist([roi_hsv], [0, 1], None, [18, 24], [0, 180, 0, 256])
    cv.normalize(roiHist, roiHist, 0, 255, cv.NORM_MINMAX)
    dst = cv.calcBackProject([target_hsv],[0, 1],roiHist,[0, 180, 0, 256],1)
    cv.imshow("back_projection_demo",dst)

print("---------------Hello Python-------------")
src = cv.imread('E:/image/HistTest.jpg')
#cv.namedWindow("Input Image", cv.WINDOW_NORMAL)
#cv.imshow("Input Image", src)
back_projection_demo()
cv.waitKey(0)

cv.destroyWindow("Input Image")