# image sharpening
import cv2
import numpy as np
img=cv2.imread('Lena.png')
cv2.imshow('original',img)
kernel_sharpening=np.array([[-1,-1,-1,-1,-1],

                            [-1,-1,-1,-1,-1],
                            [-1,-1,25,-1,-1],
                            [-1,-1,-1,-1,-1],
                            [-1,-1,-1,-1,-1]])

sharped=cv2.filter2D(img,-1,kernel_sharpening)
cv2.imshow('sharped',sharped)
cv2.waitKey(0)
cv2.destroyAllWindows()
