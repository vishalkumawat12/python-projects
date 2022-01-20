# edge detection using webcam
import cv2



def sketch(image):
    # convert to grayscale
    img_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # clean up image using Guassian Blur
    img_gray_blur = cv2.GaussianBlur(img_gray, (5, 5), 0)
    # extract edges
    canny_edges = cv2.Canny(img_gray_blur, 10, 70)
    # show result
    ret,mask=cv2.threshold(canny_edges,127,255,cv2.THRESH_BINARY)
    return mask
cap=cv2.VideoCapture(0)
while True:
    ret,frame=cap.read()
    cv2.imshow('Our live sketch',sketch(frame))
    if cv2.waitKey(1)==13:
        break

cap.release()
cv2.destroyAllWindows()