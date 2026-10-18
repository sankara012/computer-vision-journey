#### DAY 21: IMAGE ROTATION AND TRANSLATION
## CHALLENGE: rotate an image by 45°, then translate it 50px right and 30px down

import cv2
import numpy as np
img = cv2.imread("img.png")
h,w = img.shape[:2]
center = (w/2,h/2)

#The rotation part
M = cv2.getRotationMatrix2D(center,-45,1.0)   #The rotation matrix
rotated = cv2.warpAffine(img,M,(w,h)) #Applying the rotation matrix to the original image

#The translation part
T = np.float32([[1,0,50],[0,1,30]]) #The translation matrix
moved = cv2.warpAffine(rotated,T,(w,h)) #Applying the translation matrix to the rotated image

#Showing up the original,Rotated, and rotated+translated images
cv2.imshow("original", img) #Displaying the original image
cv2.imshow("rotated 45", rotated) #Displaying the rotated image
cv2.imshow("rotated + translated", moved) #Displaying the rotated+translated image
cv2.waitKey(0)
cv2.destroyAllWindows()