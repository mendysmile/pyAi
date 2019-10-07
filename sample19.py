import cv2 as cv
import numpy as np


def laplacian_demo(image):
    #dst = cv.Laplacian(image, cv.CV_32F)
    #lpls = cv.convertScaleAbs(dst)
    kernel = np.array([[0,1,0],[1,-4,1],[0,1,0]])
    dst = cv.filter2D(image,cv.CV_32F, kernel = kernel)
    lpls = cv.convertScaleAbs(dst)
    cv.imshow("laplacian_demo",lpls)


print("----------- Hello Python ------------")
src = cv.imread("E:/image/lena_color.jpg")                   # 讀取圖檔
cv.imshow("Input Image",src)                         # 顯示圖片
cv.namedWindow("Input Image",cv.WINDOW_AUTOSIZE)     # 自動調整視窗大小
laplacian_demo(src)
cv.waitKey(0)                                        # 等待使用者按按鍵

cv.destroyWindow("Input Image")                      # 關閉視窗



"""
def sobel_demo(image):
    #grad_x = cv.Sobel(image,cv.CV_32F,  1, 0)
    grad_x = cv.Scharr(image, cv.CV_32F, 1, 0)      #Sobel 的增強版
    #grad_y = cv.Sobel(image, cv.CV_32F, 0, 1)
    grad_y = cv.Scharr(image, cv.CV_32F, 0, 1)
    gradx = cv.convertScaleAbs(grad_x)
    grady = cv.convertScaleAbs(grad_y)
    cv.imshow("gradient-x", gradx)
    cv.imshow("gradient-y", grady)

    gradxy = cv.addWeighted(gradx, 0.5, grady, 0.5, 0)
    cv.imshow("gradient", gradxy)
"""
