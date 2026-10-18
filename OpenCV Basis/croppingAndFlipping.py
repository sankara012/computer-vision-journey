import cv2
import numpy as np
img = cv2.imread("img.png")
h,w = img.shape[:2]
cy, cx = h//2, w//2
crop = img[cy - 75 : cy + 75, cx - 100 : cx + 100].copy()
flip_h = cv2.flip(crop, 1)
flip_v = cv2.flip(crop, 0)
flip_both = cv2.flip(crop, -1)
print("Crope,Horizontal,Vertical,Both: ",crop.shape, flip_h.shape, flip_v.shape, flip_both.shape)
cv2.imshow("crop", crop)
cv2.imshow("horizontal flip", flip_h)
cv2.imshow("vertical flip", flip_v)
cv2.imshow("flip both", flip_both)
cv2.waitKey(0)
cv2.destroyAllWindows()

