# image transpose using opencv
import cv2
import numpy as np

img=cv2.imread('lena.png')
trasposed_img=cv2.transpose(img)
cv2.imshow('original',img)
cv2.imshow('transposed',trasposed_img)
cv2.waitKey(0)
cv2.destroyAllWindows()

