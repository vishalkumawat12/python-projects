# image airthmetic operations
import cv2
import numpy as np
img=cv2.imread('lena.png')
cv2.imshow('lena',img)
cv2.waitKey(0)
M=np.ones(img.shape,dtype='uint8')*150
added=cv2.add(img,M)
cv2.imshow('added',added)
cv2.waitKey(0)
subtracted=cv2.subtract(img,M)
cv2.imshow('subtracted',subtracted)
cv2.waitKey(0)
multiplied=cv2.multiply(img,M)
cv2.imshow('multiplied',multiplied)
cv2.waitKey(0)
divided=cv2.divide(img,M)
cv2.imshow('divided',divided)
cv2.waitKey(0)

cv2.destroyAllWindows()