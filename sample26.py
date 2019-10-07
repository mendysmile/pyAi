import cv2 as cv
import numpy as np


def top_hat_demo(image):
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    kernel = cv.getStructuringElement(cv.MORPH_RECT, (5, 5))  # 定義結構元素
    dst = cv.morphologyEx(gray, cv.MORPH_TOPHAT, kernel)  # 進行頂帽運算
    cimage = np.array(gray.shape, np.uint8)               # 新增一個一樣大的矩陣圖形
    cimage = 125                                          # 內容設成 125
    dst = cv.add(dst, cimage)                             # 兩張圖相加
    cv.imshow("tophat imag", dst)


def black_hat_demo(image):
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    kernel = cv.getStructuringElement(cv.MORPH_RECT, (5, 5))  # 定義結構元素
    dst = cv.morphologyEx(gray, cv.MORPH_BLACKHAT, kernel)  # 進行黑帽運算
    cimage = np.array(gray.shape, np.uint8)               # 新增一個一樣大的矩陣圖形
    cimage = 125                                          # 內容設成 125
    dst = cv.add(dst, cimage)                             # 兩張圖相加
    cv.imshow("blackhat imag", dst)


print("----------- Hello Python ------------")
src = cv.imread("E:/image/lena_color.jpg")   # 讀取圖檔
cv.imshow("Input Image",src)                         # 顯示圖片
cv.namedWindow("Input Image",cv.WINDOW_AUTOSIZE)     # 自動調整視窗大小
black_hat_demo(src)
cv.waitKey(0)                                        # 等待使用者按按鍵
cv.destroyWindow("Input Image")                      # 關閉視窗
