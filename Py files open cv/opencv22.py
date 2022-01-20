# color filter and bitwise opration
import cv2
import numpy as np
cap=cv2.VideoCapture(0)

while True:
    ret,frame=cap.read()

    hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)

    lower=np.array([110,50,50])
    upper=np.array([130,255,255])
    mask=cv2.inRange(hsv,lower,upper)

    result1=cv2.bitwise_and(frame,frame,mask=mask)

    cv2.imshow("show ",mask)

    cv2.imshow("result",result1)

    cv2.imshow("show 1",frame)

    if cv2.waitKey(1)==13:
        break

cap.release()

cv2.destroyAllWindows()