####FACE DETECTION######
import cv2
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
fc=cv2.CascadeClassifier("Resources/haarcascade_frontalface_default.xml")
img=cv2.imread('Resources/me.jpg')
imggrey=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
fcs = face_cascade.detectMultiScale(imggrey,1.1,4)
for (x,y,w,h) in fcs:
    cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)

cv2.imshow("Result",img)
cv2.waitKey(0)
