# image resi using pyramid 

import cv2
import numpy as np
img=cv2.imread('lena.png')
smaller=cv2.pyrDown(img)
larger=cv2.pyrUp(img)
cv2.imshow('original',img)
cv2.imshow('smaller',smaller)
cv2.imshow('larger',larger)
cv2.waitKey(0)
cv2.destroyAllWindows()