import numpy as np
import cv2
import random
img = cv2.imread("nux.png",0)
cv2.imshow("Original",img)
blur = cv2.bilateralFilter(img,5,5,10)
can=cv2.Canny(img,200,300)
can=cv2.GaussianBlur(can,(11,11),0)
x=cv2.add(blur,can)
k=np.array([[-1,1,-1],[1,1,1],[-1,1,-1]])
x=cv2.filter2D(x,-1,k)
thresh = cv2.adaptiveThreshold(x, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 205, 1)
_, contours, _ = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
filtered = []
for c in contours:
        if cv2.contourArea(c) < 10:continue
        filtered.append(c)
objects = np.zeros([img.shape[0],img.shape[1],3], 'uint8')
for c in filtered:
        cv2.drawContours(objects,[c], -1, (255,255,255), 1)

cv2.imshow("Output",objects)
cv2.waitKey(0)
cv2.destroyAllWindows()
