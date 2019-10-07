import cv2 as cv
import numpy as np


def Gradient_demo(image):
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    kernel = cv.getStructuringElement(cv.MORPH_RECT, (5, 5))  # 定義結構元素
    dst = cv.morphologyEx(gray, cv.MORPH_GRADIENT, kernel)  # 進行梯度運算
    cv.imshow("Gradient_demo", dst)


def gradient2_demo(image):
    kernel = cv.getStructuringElement(cv.MORPH_RECT, (3, 3))  # 定義結構元素
    dm = cv.dilate(image,kernel)          # 膨脹
    em = cv.erode(image,kernel)           # 腐蝕
    dst1 = cv.subtract(dm,image)          # 外部梯度
    dst2 = cv.subtract(image,em)          # 內部梯度
    cv.imshow("internal", dst2)
    cv.imshow("external", dst1)


print("----------- Hello Python ------------")
src = cv.imread("E:/image/GradientSample.jpg")   # 讀取圖檔
cv.imshow("Input Image",src)                         # 顯示圖片
cv.namedWindow("Input Image",cv.WINDOW_AUTOSIZE)     # 自動調整視窗大小
gradient2_demo(src)
cv.waitKey(0)                                        # 等待使用者按按鍵
cv.destroyWindow("Input Image")                      # 關閉視窗