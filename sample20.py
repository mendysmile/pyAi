import cv2 as cv
import numpy as np


def edge_demo(image):
    blurred = cv.GaussianBlur(image,(3,3),0)
    gray = cv.cvtColor(blurred,cv.COLOR_BGR2GRAY)
    # X Gradient
    xgrad = cv.Sobel(gray,cv.CV_16SC1,1,0)
    # Y Gradient
    ygrad = cv.Sobel(gray, cv.CV_16SC1, 0, 1)
    #edge
    edge_output = cv.Canny(gray,50,150)
    cv.imshow("Canny Edge",edge_output)

    dst = cv.bitwise_and(image,image,mask= edge_output)
    cv.imshow("Color Edge",dst)



print("----------- Hello Python ------------")
src = cv.imread("E:/image/lena_color.jpg")                   # 讀取圖檔
cv.imshow("Input Image",src)                         # 顯示圖片
cv.namedWindow("Input Image",cv.WINDOW_AUTOSIZE)     # 自動調整視窗大小
edge_demo(src)
cv.waitKey(0)                                        # 等待使用者按按鍵

cv.destroyWindow("Input Image")                      # 關閉視窗