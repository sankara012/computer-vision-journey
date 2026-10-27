###DAY31: Practice day
##CHALLENGE3: Load an image -> crop the center 200x200 -> rotate it 90 clockwise -> paste it onto a blank white canvas at a random position

import cv2
import random
import numpy as np

img = cv2.imread("cat.png")
h,w = img.shape[:2]
cy, cx = h//2, w//2
crop = img[cy-100:cy+100, cx-100:cx+100]
rotated = cv2.rotate(crop,cv2.ROTATE_90_CLOCKWISE)

#Building the canvas image of 500x500
canvas = np.full((500, 500, 3), 255, dtype=np.uint8)
ch, cw = rotated.shape[:2]          # 200, 200
canvas_h, canvas_w = canvas.shape[:2]
x = random.randint(0, canvas_w - cw)
y = random.randint(0, canvas_h - ch)
canvas[y:y+ch, x:x+cw] = rotated

#Displaying the results
cv2.imshow("Canvas image",canvas)
cv2.imshow("Crop image",crop)
cv2.imshow("Rotated image",rotated)
cv2.imwrite("challenge4.png", canvas)
cv2.waitKey(0)
cv2.destroyAllWindows()
