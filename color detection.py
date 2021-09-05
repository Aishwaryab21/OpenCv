##Color detection

import cv2
import numpy as np
def empty(a):
    pass
path='Resources/Lamp.png'
cv2.namedWindow("Trackbars")
cv2.resizeWindow("Trackbars",640,240)
cv2.createTrackbar("Hue Min","Trackbars",0,179,empty)
cv2.createTrackbar("Hue Max","Trackbars",179,179,empty)
cv2.createTrackbar("Sat Min","Trackbars",166,255,empty)
cv2.createTrackbar("Sat Max","Trackbars",241,255,empty)
cv2.createTrackbar("Val Min","Trackbars",178,255,empty)
cv2.createTrackbar("Val Max","Trackbars",255,255,empty)

while True:
    img = cv2.imread(path)
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    hmin = cv2.getTrackbarPos("Hue Min","Trackbars")
    hmax = cv2.getTrackbarPos("Hue Max","Trackbars")
    smin = cv2.getTrackbarPos("Sat Min","Trackbars")
    smax = cv2.getTrackbarPos("Sat Max","Trackbars")
    vmin = cv2.getTrackbarPos("Val Min","Trackbars")
    vmax = cv2.getTrackbarPos("Val Max","Trackbars")
    print(hmin,hmax,smin,smax,vmin,vmax)

    low=np.array([hmin,smin,vmin])
    up=np.array([hmax,smax,vmax])
    mask = cv2.inRange(hsv, low, up)
    imgr=cv2.bitwise_and(img,img,mask=mask)
    cv2.imshow("Image",img)
    cv2.imshow("HSV", hsv)
    cv2.imshow("Mask",mask)
    cv2.imshow("Result",imgr)
    hor=np.hstack((img,hsv,imgr))
    cv2.imshow("output",hor)
    cv2.waitKey(1)
