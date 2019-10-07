import cv2 as cv
import numpy as np

def measure_object(image):
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    ret, binary = cv.threshold(gray, 0, 255, cv.THRESH_BINARY | cv.THRESH_OTSU)  # 二值化 (因為背景是白色, 所以這邊我用了 THRESH_BINARY_INV)
    cv.imshow("binary imag", binary)
    dst = cv.cvtColor(binary,cv.COLOR_GRAY2BGR)
    contours, hireachy = cv.findContours(binary, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
    for i, contour in enumerate(contours):
        area = cv.contourArea(contour)              #得到輪廓的面積
        x,y ,w, h = cv.boundingRect(contour)             #得到輪廓的外接矩形
        mm = cv.moments(contour)                    #函數cv2.moments()會計算得到的矩以一個字典的形式返回
        rate = min(w,h)/max(w,h)                    # 計算寬高比
        print("rectangle rate %s" % rate)
        type(type(mm))
        cx = mm['m10'] / mm['m00']                    # 計算 cx
        cy = mm['m01'] / mm['m00']                    # 計算 cy
        cv.circle(dst,(np.int(cx),np.int(cy)),3,(0,0,255),-1)
        #cv.rectangle(dst,(x,y),(x+w,y+h),(0,0,255),2)
        print("Contours area %s"%area)             # 計算面積
        approxCurve = cv.approxPolyDP(contour,4,True)
        print(approxCurve.shape)
        # 多邊形擬合，可以用來分出圖形，主要是依靠每個圖形的邊緣需要多少折線擬合
        if approxCurve.shape[0] > 6 :
            cv.drawContours(dst, contours, i, (0,255,0),2)
        if approxCurve.shape[0] == 4:
            cv.drawContours(dst, contours, i, (0, 255, 255), 2)
    cv.imshow("detect contours", dst)


print("----------- Hello Python ------------")
src = cv.imread("E:/image/ContourImage.png")   # 讀取圖檔
cv.imshow("Input Image",src)                         # 顯示圖片
cv.namedWindow("Input Image",cv.WINDOW_AUTOSIZE)     # 自動調整視窗大小
measure_object(src)
cv.waitKey(0)                                        # 等待使用者按按鍵

cv.destroyWindow("Input Image")                      # 關閉視窗