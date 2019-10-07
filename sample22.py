import cv2 as cv
import numpy as np


def detect_hough_circle_demo(image):
    # 霍夫圆检测對燥聲敏感，邊缘檢测消噪
    dst = cv.pyrMeanShiftFiltering(image, 10, 100)      # 邊缘保留滤波EPF (這步去掉看看結果)
    gray = cv.cvtColor(dst, cv.COLOR_BGR2GRAY)          # 變成灰度圖像
    circles = cv.HoughCircles(gray, cv.HOUGH_GRADIENT, 1, 20, param1=40, param2=30, minRadius=0, maxRadius=0)
    circles = np.uint16(np.around(circles))             #把circles包含的圆心和半徑的值變成整數
    for i in circles[0, :]:
        cv.circle(image, (i[0], i[1]), i[2], (0, 0, 255), 2)      #劃出圓
        cv.circle(image, (i[0], i[1]), 2, (255, 0, 0), 2)         #劃出圓心
    cv.imshow("circle image", image)


print("----------- Hello Python ------------")
src = cv.imread("E:/image/CircleDetection004.png")   # 讀取圖檔
cv.imshow("Input Image",src)                         # 顯示圖片
cv.namedWindow("Input Image",cv.WINDOW_AUTOSIZE)     # 自動調整視窗大小
detect_hough_circle_demo(src)
cv.waitKey(0)                                        # 等待使用者按按鍵

cv.destroyWindow("Input Image")                      # 關閉視窗
