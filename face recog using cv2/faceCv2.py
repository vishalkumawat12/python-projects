import cv2
import numpy as np

face_Classifier = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')


def face_extractor(img):
    cv2.imshow("window",img)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_Classifier.detectMultiScale(gray, 1.3, 5)
    if faces is ():
        return None

    for (x, y, w, h) in faces:
        cropped_face = img[y:y + h, x:x + w]
    return cropped_face


cap = cv2.VideoCapture(0)
count = 0

while True:
    ret, frame = cap.read()
    if face_extractor(frame) is not None:
        count += 1
        face = cv2.resize(face_extractor(frame), (200, 200))
        face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)
        file_name_path = 'database/user' + str(count) + '.jpg'
        cv2.imwrite(file_name_path, face)
        cv2.putText(face, str(count), (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
        cv2.imshow('Face Cropper', face)
    else:
        print("face not found ")
        pass

    if cv2.waitKey(1) == 13 or count==100:
        break

cap.release()
cv2.destroyWindow()
print("all work is done")
