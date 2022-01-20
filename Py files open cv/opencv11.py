# image rezing using opencv
import cv2
import numpy as np
img=cv2.imread('lena.png')
cv2.imshow('original',img)
# img_scalled=cv2.resize(img,(int(img.shape[1]/2),int(img.shape[0]/2)))
# cv2.imshow('scalled',img_scalled)
# img_scalled1=cv2.resize(img,None,fx=0.5,fy=0.5)
# cv2.imshow('scalled-linear Interplotation',img_scalled1)

# img_scalled2=cv2.resize(img,None,fx=2,fy=2,interpolation=cv2.INTER_CUBIC)
# cv2.imshow('scalled-cubic Interplotation',img_scalled2)
# cv2.waitKey(0)
img_scalled3=cv2.resize(img,(900,400),interpolation=cv2.INTER_AREA)
cv2.imshow('scalled-area Interplotation',img_scalled3)
cv2.waitKey(0)
cv2.destroyAllWindows()