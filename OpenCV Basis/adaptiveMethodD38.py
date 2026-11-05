##DAY38:Thresholding with the Adaptive Method
##Challenge:  build a Day 12 gradient with dark shapes on it, then compare a single global threshold with an
#adaptive one.

import cv2
import numpy as np

H, W = 200, 400

# --- Build the test image: gradient background with dark shapes (Day 12 skills) ---
bg = np.tile(np.linspace(60, 230, W), (H, 1))
shapes = np.zeros((H, W), dtype=np.uint8)
cv2.rectangle(shapes, (20, 30), (50, 80), 255, -1)
cv2.circle(shapes, (110, 120), 22, 255, -1)
cv2.rectangle(shapes, (170, 40), (200, 150), 255, -1)
cv2.circle(shapes, (260, 70), 20, 255, -1)
cv2.rectangle(shapes, (310, 100), (340, 170), 255, -1)
cv2.circle(shapes, (370, 40), 15, 255, -1)
img = bg.copy()
img[shapes > 0] = bg[shapes > 0] - 50          # shapes are 50 levels darker than their surroundings
img = img.astype(np.uint8)

# --- Global thresholds ---
_, global_127 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY_INV)
t, global_otsu = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)

# --- Adaptive threshold ---
adaptive = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY_INV, 31, 10)

# --- Score each one against the truth ---
truth = shapes > 0
for name, m in [("global 127", global_127), ("Otsu", global_otsu), ("adaptive", adaptive)]:
    pred = m == 255
    print(name, "found %.1f%% of shape pixels, false alarms %.1f%% of image" %
          (100 * (pred & truth).sum() / truth.sum(), 100 * (pred & ~truth).sum() / pred.size))

cv2.imshow("img | global 127", np.hstack([img, global_127]))
cv2.imshow("global Otsu | adaptive", np.hstack([global_otsu, adaptive]))
cv2.waitKey(0)
cv2.destroyAllWindows()