# image blurring using opencv
import cv2
import numpy as np
img=cv2.imread('lena.png')
cv2.imshow('original',img)
cv2.waitKey(0)
kernal_3x3=np.ones((3,3),np.float32)/9
bluerred=cv2.filter2D(img,-1,kernal_3x3)
cv2.imshow('bluerred',bluerred)
cv2.waitKey(0)
kernal_5x5=np.ones((5,5),np.float32)/25
bluerred=cv2.filter2D(img,-1,kernal_5x5)
cv2.imshow('bluerred',bluerred)
cv2.waitKey(0)
cv2.destroyAllWindows()