#### DAY 21: IMAGE ROTATION AND TRANSLATION
## CHALLENGE2: Applying rotation+translation on a cat image
import cv2
import numpy as np
cat = cv2.imread("cat.png")
w, h = cat.shape[:2]
center = (w // 2, h // 2)
M = cv2.getRotationMatrix2D(center, 90, 1.0)
catRotated = cv2.warpAffine(cat, M, (w, h))

T = np.float32([[1, 0, 60], [0, 1, 40]])
moved = cv2.warpAffine(catRotated, T, (w, h))

cv2.imshow("original", cat) #Displaying the original image
cv2.imshow("rotated 45", catRotated) #Displaying the rotated image
cv2.imshow("rotated + translated", moved) #Displaying the rotated+translated image
cv2.waitKey(0)
cv2.destroyAllWindows()