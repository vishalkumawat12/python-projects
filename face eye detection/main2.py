from ast import While
import numpy as np
import cv2
from sqlalchemy import true

face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
eye_cascade = cv2.CascadeClassifier("haarcascade_eye.xml")
smile_cascade = cv2.CascadeClassifier('haarcascade_smile.xml')
# img=cv2.imread('baby.jpg')
cap = cv2.VideoCapture(0)
while True:
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.1, 10)
    # Drawing rectangle around the face
    for(x, y,  w,  h) in faces:

        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 3)
        roi_gray = gray[y:(y+h), x:(x+w)]
        roi_color = frame[y:(y+h), x:(x+w)]
        eyes = eye_cascade.detectMultiScale(roi_gray, 1.1, 10)
        eyes = eye_cascade.detectMultiScale(roi_gray, 1.1, 10)
        smile = smile_cascade.detectMultiScale(roi_gray, 1.8, 20)

        for (x_smile, y_smile, w_smile, h_smile) in smile:
            cv2.rectangle(roi_color, (x_smile, y_smile), (x_smile +
                          w_smile, y_smile + h_smile), (255, 0, 130), 3)
        for (x_eye, y_eye, w_eye, h_eye) in eyes:
            cv2.rectangle(roi_color, (x_eye, y_eye),
                          (x_eye+w_eye, y_eye+h_eye), (0, 0, 255), 3)
    cv2.imshow("Output", frame)
    if cv2.waitKey(1) == 13:
        break

cv2.waitKey(0)
cv2.destroyAllWindows()
