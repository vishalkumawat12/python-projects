import cv2
img = cv2.imread('hii.png')

img_HSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

cv2.imshow('hsv image', img_HSV)

cv2.imshow('Hue channel ', img_HSV[:, :, 0])
cv2.imshow('Saturation ', img_HSV[:, :, 1])
cv2.imshow('Value channel ', img_HSV[:, :, 2])

cv2.waitKey(0)
