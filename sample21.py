import cv2 as cv
import numpy as np

#標準霍夫線變換
def line_detection(image):
    gray = cv.cvtColor(image, cv.COLOR_RGB2GRAY)
    edges = cv.Canny(gray, 50, 150, apertureSize=3)       # apertureSize參數默認其實就是3
    cv.imshow("edges", edges)
    lines = cv.HoughLines(edges, 1, np.pi / 180, 180)
    for line in lines:
        rho, theta = line[0]                           # line[0]存儲的是點到直線的極徑和極角，其中極角是弧度表示的。
        a = np.cos(theta)                              # theta是弧度
        b = np.sin(theta)
        x0 = a * rho                                   # 代表x = r * cos（theta）
        y0 = b * rho                                   # 代表y = r * sin（theta）
        x1 = int(x0 + 1000 * (-b))                     # 計算直線起點橫坐標
        y1 = int(y0 + 1000 * a)                        # 計算起始起點縱坐標
        x2 = int(x0 - 1000 * (-b))                     # 計算直線終點橫坐標
        y2 = int(y0 - 1000 * a)     # 計算直線終點縱坐標    註：這裏的數值1000給出了畫出的線段長度範圍大小，數值越小，畫出的線段越短，數值越大，畫出的線段越長
        cv.line(image, (x1, y1), (x2, y2), (0, 0, 255), 2)  # 點的坐標必須是元組，不能是列表。
    cv.imshow("image-lines", image)


#統計概率霍夫線變換
def line_detect_possible_demo(image):
    gray = cv.cvtColor(image, cv.COLOR_RGB2GRAY)
    edges = cv.Canny(gray, 50, 150, apertureSize=3)  # apertureSize參數默認其實就是3
    lines = cv.HoughLinesP(edges, 1, np.pi / 180, 10, minLineLength=60, maxLineGap=5)
    for line in lines:
        x1, y1, x2, y2 = line[0]
        cv.line(image, (x1, y1), (x2, y2), (0, 0, 255), 2)
    cv.imshow("line_detect_possible_demo",image)


print("----------- Hello Python ------------")
src = cv.imread("E:/image/LineDetection1.png")                   # 讀取圖檔
cv.imshow("Input Image",src)                         # 顯示圖片
cv.namedWindow("Input Image",cv.WINDOW_AUTOSIZE)     # 自動調整視窗大小
line_detect_possible_demo(src)
cv.waitKey(0)                                        # 等待使用者按按鍵

cv.destroyWindow("Input Image")                      # 關閉視窗