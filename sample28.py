import cv2 as cv
import numpy as np


def watershed_demo(image):
    print(image.shape)
    blurrd = cv.pyrMeanShiftFiltering(image, 10, 100)  # 去燥聲
    # gray\binary image
    gray = cv.cvtColor(blurrd, cv.COLOR_BGR2GRAY)
    ret, binary = cv.threshold(gray, 0, 255, cv.THRESH_BINARY|cv.THRESH_OTSU)
    cv.imshow("binary-image",binary)
     # morphology operation
    kernel = cv.getStructuringElement(cv.MORPH_RECT,(3,3))
    mb = cv.morphologyEx(binary, cv.MORPH_OPEN, kernel, iterations=2)     # opening 連做兩次
    cv.imshow("opening", mb)
    sure_bg = cv.dilate(mb,kernel, iterations=3)     # iterations指的是膨脹次数
    cv.imshow("mor-opt",sure_bg)
    # 距離變換
    dist = cv.distanceTransform(mb, cv.DIST_L2,3)         # DIST_L2 慘考某文獻計算方法
    dist_output = cv.normalize(dist,0,1.0,cv.NORM_MINMAX)
    cv.imshow("distance-t", dist_output*50)
    ret, surface = cv.threshold(dist, dist.max()*0.6, 255, cv.THRESH_BINARY)
    cv.imshow("surface-bin",surface)
    surface_fg = np.uint8(surface)                        # float 轉 int
    unknown = cv.subtract(sure_bg,surface_fg)             # 膨脹後的圖減去做完二值化後的圖
    ret, markers = cv.connectedComponents(surface_fg)
    print(ret)
    # watershed transform
    markers = markers + 1                    # 讓背景不要是 0 而是 1
    markers[unknown == 255] = 0              # 讓不知道的區域變成 0
    markers = cv.watershed(src, markers)     # 邊界區域將被標記為 -1。
    image[markers == -1] = [0,0,255]
    cv.imshow("result",image)


print("----------- Hello Python ------------")
src = cv.imread("E:/image/CircleDetection004.png")   # 讀取圖檔
cv.imshow("Input Image",src)                         # 顯示圖片
cv.namedWindow("Input Image",cv.WINDOW_AUTOSIZE)     # 自動調整視窗大小
watershed_demo(src)
cv.waitKey(0)                                        # 等待使用者按按鍵
cv.destroyWindow("Input Image")                      # 關閉視窗



"""
def watershed_demo(image):
    print(image.shape)
    blurrd = cv.pyrMeanShiftFiltering(image,10,100)      #去燥聲
    # gray\binary image
    gray = cv.cvtColor(blurrd, cv.COLOR_BGR2GRAY)
    ret, binary = cv.threshold(gray, 0, 255, cv.THRESH_BINARY|cv.THRESH_OTSU)
    cv.imshow("binary-image",binary)
    # morphology operation
    kernel = cv.getStructuringElement(cv.MORPH_RECT,(3,3))
    mb = cv.morphologyEx(binary, cv.MORPH_OPEN, kernel, iterations=2)
    cv.imshow("opening", mb)
    sure_bg = cv.dilate(mb,kernel, iterations=3)     # iterations指的是膨脹次数
    cv.imshow("mor-opt",sure_bg)

    # 距離變換
    dist = cv.distanceTransform(mb, cv.DIST_L2,3)         # DIST_L2 慘考某文獻計算方法
    dist_output = cv.normalize(dist,0,1.0,cv.NORM_MINMAX)
    cv.imshow("distance-t", dist_output*50)

    ret, surface = cv.threshold(dist, dist.max()*0.6, 255, cv.THRESH_BINARY)
    cv.imshow("surface-bin",surface)
    surface_fg = np.uint8(surface)
    unknown = cv.subtract(sure_bg,surface_fg)
    ret, markers = cv.connectedComponents(surface_fg)
    print(ret)
    # watershed transform
    markers = markers + 1
    markers[unknown == 255] = 0
    markers = cv.watershed(src, markers*markers)
    image[markers == -1] = [0,0,255]
    cv.imshow("result",image)
"""