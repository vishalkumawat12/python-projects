import cv2

img=cv2.imread('1.jpg')
print(img.shape)

cv2.waitKey(0)
cv2.destroyAllWindows()
