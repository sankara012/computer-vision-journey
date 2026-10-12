#### WEEK4(PHASE2) ####
### DAY 22:DRAWING SHAPES
##CHALLENGE:  draw a rectangle and circle on a blank canvas (np.zeros) at specific coordinates

import cv2
import numpy as np

canvas = np.zeros((400, 600, 3), dtype=np.uint8)    # 400 tall, 600 wide

cv2.rectangle(canvas, (50, 50), (250, 200), (0, 255, 0), 3)
cv2.circle(canvas, (400, 150), 60, (0, 0, 255), -1)
cv2.line(canvas, (260, 200), (400, 250), (0, 0, 255), 3)

cv2.circle(canvas, (150, 320), 40, (255, 0, 0), 3)
cv2.circle(canvas, (300, 320), 40, (255, 0, 0), -1)

cv2.imshow("Shapes", canvas)
cv2.waitKey(0)
cv2.destroyAllWindows()