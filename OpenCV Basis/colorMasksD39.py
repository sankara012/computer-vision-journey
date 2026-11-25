##DAY39:Color Masks with inRange
##Challenge: Isolate the teal body of the dolphin, then the orange brush; show the masks next to the originals.

import cv2
import numpy as np

img = cv2.imread("img.png")# blank 1
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# Step 1: probe a few points (row first, then column)
for name, (x, y) in {"head": (200, 150), "belly": (330, 300),
                     "bristles": (395, 135), "handle": (190, 430)}.items():
    print(name, hsv[y,x])

# Step 2: choosing ranges
teal_lower, teal_upper = (80, 60, 60), (100, 255, 255)
orange_lower, orange_upper = (5, 80, 80), (25, 255, 255)

teal_mask = cv2.inRange(hsv, teal_lower, teal_upper)
orange_mask = cv2.inRange(hsv, orange_lower, orange_upper)

# Step 3: showing the originals next to the masks
masks = [cv2.cvtColor(m, cv2.COLOR_GRAY2BGR) for m in (teal_mask, orange_mask)]
row = np.hstack([img] + masks)
cv2.imshow("original | teal | orange", cv2.resize(row, None, fx=0.5, fy=0.5))
cv2.waitKey(0)
cv2.destroyAllWindows()

print("teal: %.1f%% of the image" % (100 * (teal_mask > 0).mean()))
print("orange: %.1f%% of the image" % (100 * (orange_mask > 0).mean()))