import cv2 as cv
import numpy as np

def create_bgr_hist(image):
    h,w,c = image.shape
    rgbHist = np.zeros([16*16*16,1],np.float32)
    bsize = 256/16
    for row in range(h):
        for col in range(w):
            b = image[row, col, 0]
            g = image[row, col, 1]
            r = image[row, col, 2]
            index = np.int(b/bsize)*16*16 + np.int(g/bsize)*16 + np.int(r/bsize)
            rgbHist[np.int(index),0] = rgbHist[np.int(index),0] +1
        return rgbHist

def hist_comp(image1,image2):
    hist1 = create_bgr_hist(image1)
    hist2 = create_bgr_hist(image2)
    match1 = cv.compareHist(hist1,hist2,cv.HISTCMP_BHATTACHARYYA)
    match2 = cv.compareHist(hist1, hist2, cv.HISTCMP_CORREL)
    match3 = cv.compareHist(hist1, hist2, cv.HISTCMP_CHISQR)
    print("巴式距離:%s 相關性:%s 卡方:%s"%(match1,match2,match3))

print("---------------Hello Python-------------")
src1 = cv.imread('E:/image/Image1.jpg')
src2 = cv.imread('E:/image/Image1.jpg')
cv.namedWindow("Input Image", cv.WINDOW_NORMAL)
cv.imshow("Input Image", src1)
hist_comp(src1,src2)
cv.waitKey(0)
cv.destroyWindow("Input Image")