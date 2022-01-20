# image rotation using opencv
import cv2
import numpy as np
img=cv2.imread('Lena.png')
height,width=img.shape[:2] # get the height and width of the image
rotation_matrix=cv2.getRotationMatrix2D((width/2,height/2),90,.7) # get the rotation matrix
Rotated_image=cv2.warpAffine(img,rotation_matrix,(width,height)) # rotate the image
cv2.imshow('Original',img)
cv2.imshow('Rotated',Rotated_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
