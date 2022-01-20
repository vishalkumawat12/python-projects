import cv2
img=cv2.imread('1.jpg')
cv2.imshow("myimg",img)
cv2.waitKey(0)
cv2.imwrite('hii.png',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
