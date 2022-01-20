# Image edge detection using opencv in python
import cv2
img=cv2.imread("Lena.png",0)

height,width=img.shape

sobel_x=cv2.Sobel(img,cv2.CV_64F,1,0,ksize=5)

sobel_y = cv2.Sobel(img, cv2.CV_64F, 0, 1, ksize=5)
cv2.imshow('orignal Image',img)
cv2.waitKey(0)

cv2.imshow("sobel x image ",sobel_x)
cv2.waitKey(0)

cv2.imshow("sobel y image ", sobel_y)
cv2.waitKey(0)

sobel_Or=cv2.bitwise_or(sobel_x,sobel_y)
cv2.imshow("sobel or ", sobel_Or)
cv2.waitKey(0)


