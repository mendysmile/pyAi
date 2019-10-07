import cv2 as cv
import numpy as np

def contours_demo(image):
    dst = cv.GaussianBlur(image,(3,3),0)           #去除躁點
    gray = cv.cvtColor(dst, cv.COLOR_BGR2GRAY)
    ret, binary = cv.threshold(gray, 0, 255, cv.THRESH_BINARY | cv.THRESH_OTSU)    # 二值化
    cv.imshow("binary imag", binary)

    contours, heriachy = cv.findContours(binary, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)

    for i, contour in enumerate(contours):
        cv.drawContours(image, contours, i, (0, 0, 255), -1)
        print(i)
    cv.imshow("detect contours",image)


print("----------- Hello Python ------------")
src = cv.imread("E:/image/CircleDetection001.png")   # 讀取圖檔
cv.imshow("Input Image",src)                         # 顯示圖片
cv.namedWindow("Input Image",cv.WINDOW_AUTOSIZE)     # 自動調整視窗大小
contours_demo(src)
cv.waitKey(0)                                        # 等待使用者按按鍵

cv.destroyWindow("Input Image")                      # 關閉視窗