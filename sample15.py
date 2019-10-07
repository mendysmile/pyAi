import cv2 as cv
import numpy as np

def template_demo():
    tp1 = cv.imread("E:/image/Target2.png")
    target = cv.imread("E:/image/Sample2.png")
    cv.imshow("tp1 Image",tp1)
    cv.imshow("target image", target)
    methods = [cv.TM_SQDIFF_NORMED, cv.TM_CCORR_NORMED, cv.TM_CCOEFF_NORMED]
    th, tw = tp1.shape[:2]

    for md in methods:
        print(md)
        result = cv.matchTemplate(tp1,target,md)
        min_val,max_val,min_loc,max_loc = cv.minMaxLoc(result)
        if md == cv.TM_SQDIFF_NORMED:
            t1 = min_loc
        else:
            t1 = max_loc
        br = (t1[0]+tw,t1[1]+th);
        cv.rectangle(target,t1,br,(0,0,255),2)
        cv.imshow("match-"+np.str(md),target)
        cv.imshow("match-(result)"+np.str(md),result)

print("---------------Hello Python-------------")
src = cv.imread('E:/image/HistTest.jpg')
cv.namedWindow("Input Image", cv.WINDOW_NORMAL)
#cv.imshow("Input Image", src)
template_demo()
cv.waitKey(0)

cv.destroyWindow("Input Image")