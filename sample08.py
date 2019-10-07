import cv2 as cv
import numpy as np

def blur_demo(image):
    det = cv.blur(image,(5,5))
    cv.imshow("blur",det)

def median_blur_demo(image):
    det = cv.medianBlur(image,5)
    cv.imshow("median_blur_demo", det)

def median_blur_demo2(image):
    det = cv.medianBlur(image,7)
    cv.imshow("median_blur_demo2", det)

def custon_blur_demo(image):
    kernel = np.array([[0,-1,0],[-1,5,-1],[0,-1,0]], np.float32)
    det = cv.filter2D(image, -1 , kernel=kernel)
    cv.imshow("custon_blur_demo",det)

print("---------------Hello Python-------------")
src = cv.imread('E:/image/Image1.jpg')
cv.namedWindow("Input Image", cv.WINDOW_NORMAL)
cv.imshow("Input Image", src)
median_blur_demo(src)
median_blur_demo2(src)
custon_blur_demo(src)
cv.waitKey(0)

cv.destroyWindow("Input Image")