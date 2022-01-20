import cv2
import numpy as np
from os import listdir
from os.path import isfile, join

data_path = 'database/'
onlyfiles = [f for f in listdir(data_path) if isfile(join(data_path, f))]

traing_data, Labels = [], []
for i, files in enumerate(onlyfiles):
    image_path = data_path + onlyfiles[i]
    images = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    traing_data.append(np.asarray(images, dtype=np.uint8))
    Labels.append(i)
Labels = np.asarray(Labels, dtype=np.int32)

# pip install --user opencv-contrib-python
model = cv2.face.LBPHFaceRecognizer_create()

model.train(np.asarray(traing_data), np.asarray(Labels))
print("model trained")
face_Classifier = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')


def face_detecter(img, size=0.5):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_Classifier.detectMultiScale(gray, 1.3, 5)

    if faces is ():
        return img, []

    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 255), 2)

        roi = img[y:y+h, x:x+w]

        roi = cv2.resize(roi, (200, 200))
    return img, roi


cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    image, face = face_detecter(frame)

    try:

        face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)
        result = model.predict(face)

        if result[1] < 500:
            confidence = int(100*(1-(result[1])/300))
            display_String = str(confidence)+"%  Confidence it is user"

        cv2.putText(image, display_String, (100, 120),
                        cv2.FONT_HERSHEY_COMPLEX, 1, (150, 120, 255))

        if confidence > 60:
            cv2.putText(image, "Unlocked", (250, 420),
                        cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0))
            cv2.imshow('face cropper', image)

        else:
            cv2.putText(image, "locked", (250, 420),
                        cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0))
            cv2.imshow('face cropper', image)
    except:
        cv2.putText(image, "face not found", (250, 420),
                    cv2.FONT_HERSHEY_COMPLEX, 1, (255, 0, 0))
        

        cv2.imshow('face cropper', image)
        pass

    if cv2.waitKey(1) == 13:
        break


cap.release()
cv2.destroyAllWindows()
