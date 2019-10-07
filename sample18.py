import cv2 as cv
import numpy as np

def pyramid_demo(image):        #高斯金字塔
    level = 3
    temp = image.copy()
    pyramid_image = []
    for i in range(level):
        dst = cv.pyrDown(temp)
        pyramid_image.append(dst)
        cv.imshow("pyramid_down_"+str(i),dst)
        temp = dst.copy()
    return  pyramid_image


def Laplacian_demo(image):        #拉普拉斯金字塔（Laplacianpyramid）
    pyramid_images = pyramid_demo(image)
    level = len(pyramid_images)
    for i in range(level-1,-1,-1):     # 從 level-1 開始, 到 -1 結束, 遞增值為 -1
        if (i-1) < 0:
            expand = cv.pyrUp(pyramid_images[i], dstsize= image.shape[:2])
            lpls = cv.subtract(image,expand)
            cv.imshow("Laplacian_demo"+str(i),lpls)
        else:
            expand = cv.pyrUp(pyramid_images[i], dstsize= pyramid_images[i-1].shape[:2])
            lpls = cv.subtract(pyramid_images[i-1],expand)
            cv.imshow("Laplacian_demo"+str(i),lpls)


print("----------- Hello Python ------------")
src = cv.imread("E:/image/lena_color.jpg")                   # 讀取圖檔
cv.imshow("Input Image",src)                         # 顯示圖片
cv.namedWindow("Input Image",cv.WINDOW_AUTOSIZE)     # 自動調整視窗大小
Laplacian_demo(src)
cv.waitKey(0)                                        # 等待使用者按按鍵

cv.destroyWindow("Input Image")                      # 關閉視窗