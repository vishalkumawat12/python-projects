#  snifing tool  using python

import cv2
crop=False
ref_point=[]

def drawing(event,x,y,flags,param):
    global ref_point,crop

    if event==cv2.EVENT_LBUTTONDOWN:
        ref_point=[[x,y]]
        print(ref_point)
    elif event==cv2.EVENT_LBUTTONUP:
        ref_point.append([x,y])
        print(ref_point)
        cv2.rectangle(img,ref_point[0],ref_point[1],(0,255,0),2)
        crop=True
        cv2.imshow("image",img)

img=cv2.imread("download.png")

clone=img.copy()

cv2.namedWindow("image")
cv2.setMouseCallback("image",drawing)
while True:
    cv2.imshow("image",img)
    key=cv2.waitKey(1)
    if key==ord("q"):
        break
    elif key==ord("r"):
        img=clone.copy()
    
    elif key==ord("c"):
        break


if len(ref_point)==2:
    crop_img=clone[ref_point[0][1]:ref_point[1][1],ref_point[0][0]:ref_point[1][0]]

    cv2.imshow("crop_img",crop_img)
    cv2.waitKey(0)
cv2.destroyAllWindows()