###DAY31: Practice day
##CHALLENGE1: Loading an image,rotating it 45 degree,convert it to grayscale,draw a bounding box around the center and save the result.
import cv2
import numpy as np
img = cv2.imread("lena.png")
h, w = img.shape[:2]
cx,cy = w//2, h//2
M = cv2.getRotationMatrix2D((cx,cy),45,1.0)
rotated = cv2.warpAffine(img,M,(w,h))
gray = cv2.cvtColor(rotated, cv2.COLOR_BGR2GRAY)
cv2.rectangle(gray,(cx-100,cy-75),(cx+100,cy+75),255,2)

#Displaying the original image before the rotation
cv2.imshow("Original",img)
cv2.waitKey(0)

#Displaying the rotated image before converting it to grayscale
cv2.imshow("rotated",rotated)
cv2.waitKey(0)

#Displaying the rotated grayscale image with the rectangle at the center
cv2.imshow("Rotated grayscale image with a rectangle at the center",gray)
cv2.waitKey(0)
cv2.imwrite("rotated_gray_box.png", gray)
cv2.destroyAllWindows()