import cv2 as cv
import numpy as np

def create_image():
    img = np.zeros([400, 400, 3], np.uint8)
    img[:, :, 0] = np.zeros([400, 400]) + 255
    img[:, :, 1] = np.zeros([400, 400]) + 255
    img[:, :, 2] = np.ones([400, 400]) * 1
    cv.imshow("new image", img)

create_image()

cv.waitKey(0)
cv.destroyAllWindows()