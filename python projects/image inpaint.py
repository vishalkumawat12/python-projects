# image inpainting using deep learning and image processing techniques in python

import numpy as np
import cv2
import sys

class Sketcher:
    def __init__(self,windowName,destImg,color_func):
        self.prev_pt = None
        self.windowName = windowName
        self.destImg = destImg
        self.color_func = color_func
        self.dirty=False
        self.show()
        cv2.setMouseCallback(self.windowName,self.on_mouse)

        

    def show(self):
        cv2.imshow(self.windowName,self.destImg[0])
        cv2.imshow(self.windowName +":mask",self.destImg[1])


    def on_mouse(self,event,x,y,flags,param):
        pt = (x,y)
        if event == cv2.EVENT_LBUTTONDOWN:
          self.prev_pt = pt
        elif event ==cv2.EVENT_LBUTTONUP:
          self.prev_pt = None
        
        if self.prev_pt and flags & cv2.EVENT_FLAG_LBUTTON:
            for dest,color in zip(self.destImg,self.color_func()):
                cv2.line(dest,self.prev_pt,pt,color,5)
            self.dirty = True
            self.prev_pt = pt
            self.show()


        

def main():
    print("Usage : Python Inpaint.py <image_path>")
    print("Keys :")
    print("t - impaint using FMM")
    print("n - impaint using Ns method")
    print("r _ - reset")
    print("ESC - exit")

    img=cv2.imread("download.png",cv2.IMREAD_COLOR)
    if(img is None):
        print("Image not found")

        return

    img_mask=img.copy()
    inpaintMask=np.zeros(img.shape[:2],np.uint8)
    sketch=Sketcher("image",[img_mask,inpaintMask],lambda:((255,255,255),255))

    while True:
        ch=cv2.waitKey(0)

        if ch==27:
            break
        if ch==ord('t'):
            res=cv2.inpaint(src=img_mask,inpaintMask=inpaintMask,inpaintRadius=3,flags=cv2.INPAINT_TELEA)
            cv2.imshow("result of FMM",res)
        
        if ch==ord('n'):
            res=cv2.inpaint(src=img_mask,inpaintMask=inpaintMask,inpaintRadius=3,flags=cv2.INPAINT_NS)
            cv2.imshow("result of Ns",res)
        if ch==ord('r'):

            img_mask[:]=img
            inpaintMask[:]=0
            sketch.show()
            print("Completed")




if __name__=='__main__':
    main()

    cv2.destroyAllWindows()