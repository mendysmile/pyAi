import cv2 as cv
import numpy as np

def bi_demo(image):
    dst = cv.bilateralFilter(image,0,100,15)
    cv.imshow("bi_demo",dst)

def mean_shift_demo(image):
    dst = cv.pyrMeanShiftFiltering(image,10,30)
    cv.imshow("mean_shift_demo", dst)

def mean_shift_demo2(image):
    dst = cv.pyrMeanShiftFiltering(image,10,50)
    cv.imshow("mean_shift_demo2", dst)

print("---------------Hello Python-------------")
src = cv.imread('E:/image/bi_testImage.jpg')
#src2 = cv.imread('E:/image/Lenanoise.jpg')
cv.namedWindow("Input Image", cv.WINDOW_NORMAL)
cv.imshow("Input Image", src)
bi_demo(src)
mean_shift_demo(src)
mean_shift_demo2(src)
cv.waitKey(0)

cv.destroyWindow("Input Image")