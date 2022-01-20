# image trasformatio using python

import cv2
import numpy as np
img=cv2.imread('lena.png')
height,width=img.shape[:2]
print(height,width)
quarder_height,quarder_width=height/4,width/4
print(quarder_height,quarder_width)
# traslation matrix
T=np.float32([[1,0,quarder_width],[0,1,quarder_height]])
print(T)

# warp affine trastformation
img_translation=cv2.warpAffine(img,T,(width,height))
cv2.imshow('orignal img ',img)
cv2.imshow('img_translation',img_translation)
cv2.waitKey(0)
cv2.destroyAllWindows()

