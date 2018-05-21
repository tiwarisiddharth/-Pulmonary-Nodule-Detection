import cv2
import random
import numpy as np
i=cv2.imread('nux.png',0)
c=cv2.bilateralFilter(i,5,5,10)
can=cv2.Canny(i,150,150)
can=cv2.GaussianBlur(can,(11,11),0)
x=cv2.add(c,can)
k=np.array([[-1,1,-1],[1,1,1],[-1,1,-1]])
x=cv2.filter2D(x,-1,k)
_,x=cv2.threshold(x,191,255,cv2.THRESH_TOZERO)
cv2.imshow('s',x)
cv2.waitKey()
cv2.destroyAllWindows()
