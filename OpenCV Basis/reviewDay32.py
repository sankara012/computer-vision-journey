import cv2
import numpy as np

img = cv2.imread("lena.png")
print(img.shape)
print(img[0,0])
rectangle = cv2.rectangle(img,(0,0),(10,10),(0,255,0),-1)
h, w = img.shape[:2]
circle = cv2.circle(img, (w - 1, h - 1), 30, (0, 0, 255), -1)
T = np.float32([[1,0,50],[0,1,30]])
moved = cv2.warpAffine(img,T, (img.shape[1],img.shape[0]))
cv2.imshow("img",img)
cv2.imshow("moved",moved)
cv2.waitKey(0)
cv2.destroyAllWindows()