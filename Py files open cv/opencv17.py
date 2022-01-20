# image smoothing using python
import cv2
import numpy as np

img=cv2.imread('lena.png')
cv2.imshow('Original',img)
cv2.waitKey(0)
blur=cv2.blur(img,(3,3))
cv2.imshow('Blurred',blur)
cv2.waitKey(0)
Gaussian=cv2.GaussianBlur(img,(7,7),0)
cv2.imshow('Gaussian',Gaussian)
cv2.waitKey(0)
median=cv2.medianBlur(img,5)
cv2.imshow('Median',median)
cv2.waitKey(0)
bilateral=cv2.bilateralFilter(img,9,75,75)
cv2.imshow('Bilateral',bilateral)
cv2.waitKey(0)
cv2.destroyAllWindows()