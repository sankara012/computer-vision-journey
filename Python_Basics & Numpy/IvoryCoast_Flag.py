import cv2
import numpy as np
canvas = np.zeros((100,150,3),dtype=np.uint8)
canvas[0:100,0:50] = 	[0, 165, 255]
canvas[0:100,50:100] = [255, 255, 255]
canvas[0:100,100:150] = [0, 255, 0]

cv2.imwrite("IvoryCoast.png", canvas)
cv2.imshow("IvoryCoast", canvas)
cv2.waitKey(0)
cv2.destroyAllWindows()