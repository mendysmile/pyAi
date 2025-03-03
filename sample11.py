import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

def plot_demo(image):
    plt.hist(image.ravel(),256,[0,256])
    plt.show("直方圖")

def image_hist(image):
    color = ('blue','green','red')
    for i, color in enumerate(color):
        hist = cv.calcHist([image],[i],None,[256],[0,256])
        plt.plot(hist, color=color)
        plt.xlim([0,256])
    plt.show()

print("---------------Hello Python-------------")
src = cv.imread('E:/image/Image1.jpg')
cv.namedWindow("Input Image", cv.WINDOW_NORMAL)
cv.imshow("Input Image", src)
#plot_demo(src)
image_hist(src)
cv.waitKey(0)

cv.destroyWindow("Input Image")