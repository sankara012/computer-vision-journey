###PHASE 3:Image Processing (Days 36-63)
##DAY36: Binary Thresholding
##Challenge:  threshold the grayscale dolphin at three different values, display them side by side, and confirm
#with np.array_equal that cv2 matches the NumPy version.

import cv2
import numpy as np

img = cv2.imread("img.png")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
t, low  = cv2.threshold(gray, 80,  255, cv2.THRESH_BINARY)
t, mid  = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
t, high = cv2.threshold(gray, 200, 255, cv2.THRESH_BINARY)
row = np.hstack([gray, low, mid, high])
row = cv2.resize(row, None, fx=0.5, fy=0.5)
cv2.imshow("gray | 80 | 127 | 200", row)
cv2.waitKey(0)
cv2.destroyAllWindows()

numpy_version = np.where(gray > 127, 255, 0).astype(np.uint8)
print("matches NumPy:", np.array_equal(mid, numpy_version))
t, inv = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY_INV)
cv2.imshow("binary", inv)
cv2.waitKey(0)
print("INV equals 255 - BINARY:", np.array_equal(inv, 255 - mid))