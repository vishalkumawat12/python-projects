# color ranging using python

import cv2
import numpy as np

cap=cv2.VideoCapture(0)

while True:
    ret,frame=cap.read()

    hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)

    lower=np.array([110,50,50])
    upper=np.array([130,255,255])

    mask=cv2.inRange(hsv,lower,upper)

    cv2.imshow("show",mask)

    cv2.imshow("orignal",frame)



    if cv2.waitKey(0)=='13':
        break

cap.release()