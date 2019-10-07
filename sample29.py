import cv2 as cv
import numpy as np

def face_detect_demo(image):
    gray = cv.cvtColor(image,cv.COLOR_BGR2GRAY)
    face_detector = cv.CascadeClassifier("C:/opencv3.4/build/etc/haarcascades/haarcascade_frontalface_alt.xml")
    faces = face_detector.detectMultiScale(gray,1.1,5)
    for x, y, w, h in faces:
        cv.rectangle(image,(x,y),(x+w,y+h),(0,0,255),2)
    cv.imshow("face_detect_demo",image)

print("----------- Hello Python ------------")
#src = cv.imread("E:/image/faceDetect.jpg")   # 讀取圖檔
capture = cv.VideoCapture(0)
#cv.imshow("Input Image",src)                         # 顯示圖片
#cv.namedWindow("Input Image",cv.WINDOW_AUTOSIZE)     # 自動調整視窗大小
cv.namedWindow("face_detect_demo",cv.WINDOW_AUTOSIZE)     # 自動調整視窗大小
while(True):
    ret, frame = capture.read()
    frame = cv.flip(frame,1)
    face_detect_demo(frame)
    c = cv.waitKey(10)
    if c == 27:   # 27
        break

cv.waitKey(0)                                        # 等待使用者按按鍵
cv.destroyWindow("Input Image")                      # 關閉視窗