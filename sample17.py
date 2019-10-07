import cv2 as cv
import numpy as np


def big_image_binary(image):
    print(image.shape)                                       #超大圖像，螢幕無法顯示完整
    cw,ch = 256,256
    h,w = image.shape[:2]
    gray = cv.cvtColor(image,cv.COLOR_RGB2GRAY)              #要二值化圖像，要先進行灰度化處理
    for row in range(0,h,ch):
        for col in range(0,w,cw):
            roi = gray[row:row+ch,col:col+cw]               #獲取分塊
            print(np.std(roi), np.mean(roi))
            dst = cv.adaptiveThreshold(roi, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 127, 20)  # 自適應閥值
            gray[row:row + ch, col:col + cw] = dst          #分塊覆蓋
            print(np.std(dst),np.mean(dst))

    cv.imwrite("E:/image/result_binary.jpg",gray)
    cv.imshow("big_image_binary",gray)


print("----------- Hello Python ------------")
src = cv.imread("E:/image/B5.jpg")                   # 讀取圖檔
cv.imshow("Input Image",src)                         # 顯示圖片
cv.namedWindow("Input Image",cv.WINDOW_AUTOSIZE)     # 自動調整視窗大小
big_image_binary(src)
cv.waitKey(0)                                        # 等待使用者按按鍵

cv.destroyWindow("Input Image")                      # 關閉視窗




"""
def big_image_binary(image):
    print(image.shape)                                            #超大圖像，螢幕無法顯示完整
    cw=256
    ch=256
    h,w=image.shape[:2]
    gray=cv.cvtColor(image,cv.COLOR_BGR2GRAY)                     #要二值化圖像，要先進行灰度化處理
    for row in range(0,h,ch):
        for col in range(0,w,cw):
            roi=gray[row:row+ch,col:cw+col]                                     #獲取分塊
            print(np.std(roi),np.mean(roi))
            dst=cv.adaptiveThreshold(roi,255,cv.ADAPTIVE_THRESH_GAUSSIAN_C,cv.THRESH_BINARY,127,20)     #自適應閥值
            gray[row:row+ch,col:cw+col]=dst                                     #分塊覆盖
            print(np.std(dst),np.mean(dst))                                     #印出標準差與平均值
    cv.imshow("big_image_binary",gray)
    cv.imwrite("E:/image/result_binary.jpg",gray)
"""