import cv2 as cv
import numpy as np

def color_space_demo(image):
    gray = cv.cvtColor(image,cv.COLOR_BGR2GRAY)
    cv.imshow("gray",gray)
    hsv = cv.cvtColor(image, cv.COLOR_BGR2HSV)
    cv.imshow("hsv",hsv)
    yuv = cv.cvtColor(image, cv.COLOR_BGR2YUV)
    cv.imshow("yuv",yuv)
    YCbCr

print("-------------Hello Python-------------")
src = cv.imread("E:/image/Image1.jpg")
cv.namedWindow("Input Image", cv.WINDOW_NORMAL)
cv.imshow("Input Image", src)

cv.waitKey(0)
cv.destroyAllWindows()