import cv2 as cv
import numpy as np

def add_demo(m1,m2):
    dst =cv.add(m1,m2)
    cv.imshow('add_demo',dst)

def substract_demo(m1,m2):
    dst =cv.subtract(m1,m2)
    cv.imshow('substract_demo',dst)

def divide_demo(m1,m2):
    dst = cv.divide(m1,m2)
    cv.imshow('divide_demo',dst)

def logic_demo(m1,m2):
    dst = cv.bitwise_and(m1,m2)
    cv.imshow('logic_demo',dst)

def constrast_brightness_demo(image,c,b):
    h, w, ch= image.shape
    blank = np.zeros([h,w,ch],image.dtype)
    dst = cv.addWeighted(image,c,blank,1-c,b)
    cv.imshow('constrast_brightness_demo',dst)
    return dst

# print("-------------Hello Python-------------")
# src = cv.imread("E:/image/Image1.jpg")
# cv.namedWindow("Input Image", cv.WINDOW_NORMAL)
# #cv.imshow("Input Image", src)
# dst1 = constrast_brightness_demo(src,1.2,10)
# dst2 = constrast_brightness_demo(src,1.1,50)
# #cv.imshow('image1',dst1)
# #cv.imshow('image2',dst2)

print('---------Hello Pathon----------')
src1 = cv.imread("E:/image/WIN.jpg")
src2 = cv.imread("E:/image/LINUX.jpg")
print(src1.shape)
print(src2.shape)

cv.namedWindow("image1",cv.WINDOW_NORMAL)
cv.imshow('image1',src1)
cv.namedWindow("image2",cv.WINDOW_NORMAL)
cv.imshow('image2',src2)

#add_demo(src1,src2)
#substract_demo(src2,src1)
#substract_demo(src1,src2)
#divide_demo(src1,src2)
logic_demo(src1,src2)

cv.waitKey(0)
cv.destroyAllWindows()