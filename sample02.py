import cv2 as cv
import numpy as np

def access_pixels(image):
    print(image.shape)
    height = image.shape[0]
    width = image.shape[1]
    channel = image.shape[2]
    print("width : %s, height : %s, channel : %s" %(height,width,channel))
    for row in range(height):
        for col in range(width):
            for c in range(channel):
                pv = image[row,col,c]
                image[row,col,c] = 255-pv
    cv.imshow('access_pixels', image)

def inverse(image):
    dst = cv.bitwise_not(image)
    cv.imshow("inverse", dst)

def create_image():
    img = np.ones([400, 400, 1], np.uint8)
    img = img * 111
    cv.imshow("new image", img)
"""
    m1 = np.zeros([3,3],np.float32)
    m1.fill(123.456)
    print(m1)
    m2 = m1.reshape([1,9])
    print(m2)

    img = np.zeros([400,400,1],np.uint8)
    img[:,:,0] = np.ones([400,400])*1
    cv.imshow("new image",img)
"""
print("-------------Hello Python-------------")
src = cv.imread("E:/image/Image1.jpg")
cv.namedWindow("Input Image", cv.WINDOW_NORMAL)
cv.imshow("Input Image", src)
create_image()
#inverse(src)
"""
t1 = cv.getTickCount()
access_pixels(src)
t2 = cv.getTickCount()

time = (t2-t1)/cv.getTickFrequency()
print("Time: %s" %(time*1000))
"""
cv.waitKey(0)
cv.destroyAllWindows()
