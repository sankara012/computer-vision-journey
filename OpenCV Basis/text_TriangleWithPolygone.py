### DAY 23: DRAWING AND POLYGONS
## CHALLENGE: Draw a rectangle and circle on a blank canvas (np.zeros) at specific coordinates
import cv2
import numpy as np
canvas = np.zeros((300, 500, 3), dtype=np.uint8)
cv2.putText(canvas,"Razak Sankara",(50, 80),cv2.FONT_HERSHEY_SIMPLEX,1.5, (255, 160, 255), 2)
triangle = np.array([(150, 150), (250, 150), (200, 250)], dtype=np.int32)

#Used polylines to draws the outline
#cv2.polylines(canvas, [triangle], True, (0, 255, 0), 3)

#Used fillPoly to fill the inside
cv2.fillPoly(canvas, [triangle], (0, 255, 0))
cv2.imshow("Day 23 challenge", canvas)
cv2.waitKey(0)
cv2.destroyAllWindows()