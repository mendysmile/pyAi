import cv2 as cv
import numpy as np


def Open_demo(image):
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    ret, binary = cv.threshold(gray, 0, 255, cv.THRESH_BINARY | cv.THRESH_OTSU)  # 二值化
    cv.imshow("binary imag", binary)
    kernel = cv.getStructuringElement(cv.MORPH_RECT,(5,5))       #定義結構元素
    binary = cv.morphologyEx(binary, cv.MORPH_OPEN, kernel)               #進行開運算
    cv.imshow("Open-Result imag", binary)


def Close_demo(image):
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    ret, binary = cv.threshold(gray, 0, 255, cv.THRESH_BINARY | cv.THRESH_OTSU)  # 二值化
    cv.imshow("binary imag", binary)
    kernel = cv.getStructuringElement(cv.MORPH_RECT,(5,5))       #定義結構元素
    binary = cv.morphologyEx(binary, cv.MORPH_CLOSE, kernel)               #進行開運算
    cv.imshow("Close-Result imag", binary)


print("----------- Hello Python ------------")
src = cv.imread("E:/image/morphCloseSample.jpg")   # 讀取圖檔
cv.imshow("Input Image",src)                         # 顯示圖片
cv.namedWindow("Input Image",cv.WINDOW_AUTOSIZE)     # 自動調整視窗大小
Close_demo(src)
cv.waitKey(0)                                        # 等待使用者按按鍵

cv.destroyWindow("Input Image")                      # 關閉視窗