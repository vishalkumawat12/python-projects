import cv2
import math
pointsList = []

def mouse_callback(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        # print("x: {}, y: {}".format(x, y))
        size=len(pointsList)
        if size!=0 and size %3!=0:
            cv2.line(path,tuple(pointsList[round((size-1)/3)*3]),(x,y),(0,255,0),2)
        cv2.circle(path, (x, y), 3, (0, 0, 255), -1)
        pointsList.append((x, y))
        # print(pointsList)

def gradient(p1, p2):
    return (p2[1] - p1[1]) / (p2[0] - p1[0])

def getAngle(pointsList):
    pt1, pt2, pt3 = pointsList[0], pointsList[1], pointsList[2]
    # print(pt1, pt2, pt3)
    m1= gradient(pt1, pt2)
    m2= gradient(pt1, pt3)
    angR=math.atan((m2-m1)/(1+m1*m2))
    angD=round(math.degrees(angR))
    # print(angD)
    cv2.putText(path, str(angD), (pt1[0], pt1[1]), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)


path=cv2.imread('ang;e.jpg')
while True:
    if len(pointsList) % 3==0 and len(pointsList)>0:
        getAngle(pointsList)
    cv2.imshow('image', path)
    cv2.setMouseCallback('image', mouse_callback)

    if cv2.waitKey(1) & 0xFF== ord('q'):
        pointsList=[]
        path=cv2.imread('ang;e.jpg')

cv2.destroyAllWindows()