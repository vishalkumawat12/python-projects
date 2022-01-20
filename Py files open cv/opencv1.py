import cv2
from os import system
img=cv2.imread("1.jpg")
cv2.imshow("myimg",img)
cv2.waitKey(0)
cv2.destroyAllWindows()
system("cls")
print(img)