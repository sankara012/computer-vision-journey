##DAY40:Applying Masks with Bitwise Operations
##Challenge:Keep only the teal pixels of the dolphin on a black background, then invert the mask to keep
#everything else

import cv2
import numpy as np

img = cv2.imread("img.png")
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
teal_mask = cv2.inRange(hsv, (80, 60, 60), (100, 255, 255))          # The Day 39 range

# Part 1: keep only the teal pixels
teal_only = cv2.bitwise_and(img, img, mask=teal_mask)

# Part 2: invert the mask and keep everything else
inverted = cv2.bitwise_not(teal_mask)
rest = cv2.bitwise_and(img, img, mask=inverted)

# Check: do the two pieces rebuild the original?
rebuilt = cv2.bitwise_or(teal_only, rest)
print("rebuilt equals original:", np.array_equal(rebuilt, img))

row = np.hstack([img, teal_only, rest])
cv2.imshow("original | teal only | the rest", cv2.resize(row, None, fx=0.4, fy=0.4))
cv2.waitKey(0)
cv2.destroyAllWindows()