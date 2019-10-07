import cv2 as cv
import numpy as np



print("-------------Hello Python-------------")
src = cv.imread("E:/image/Image2.jpg")
cv.namedWindow("Input Image", cv.WINDOW_NORMAL)
cv.imshow("Input Image", src)
face = src[80:270,180:330]
#cv.imshow('face image',face)
gray = cv.cvtColor(face,cv.COLOR_BGR2GRAY)
backface = cv.cvtColor(gray,cv.COLOR_GRAY2BGR)
src[80:270,180:330] = backface
cv.imshow('face',src)

cv.waitKey(0)
cv.destroyAllWindows()