import cv2 as cv
import numpy as np

def fill_color_demo(image):
    copyimage = image.copy()
    h,w = image.shape[:2]
    mask = np.zeros([h+2,w+2],np.uint8)
    (b,g,r) = copyimage[455,250]
    print("位置(250,455)的pixel -red:%d, green:%d, blue:%d" % (r,g,b))
    cv.floodFill(copyimage,mask,(250,455),(255,0,255),(30,30,30),(10,10,10),cv.FLOODFILL_FIXED_RANGE)
    cv.imshow('fill_color_demo',copyimage)

def fill_binary():
    image = np.zeros([400,400,3],np.uint8)
    image[100:300,100:300,:] = 255
    cv.imshow('fill_binary',image)

    mask = np.ones([400+2,400+2],np.uint8)
    mask[119:281,119:281]=0
    cv.floodFill(image, mask, (200, 200), (0, 0, 255), cv.FLOODFILL_MASK_ONLY)
    cv.imshow('fill_binary',image)

print("-------------Hello Python-------------")
src = cv.imread("E:/image/Image2.jpg")
cv.namedWindow("Input Image", cv.WINDOW_NORMAL)
cv.imshow("Input Image", src)
#fill_color_demo(src)
fill_binary()
cv.waitKey(0)
cv.destroyAllWindows()