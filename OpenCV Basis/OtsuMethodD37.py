##DAY37:Thresholding with Otsu's Method
##Challenge:run Otsu on my dolphin and on a noisy image from Day 13; print the chosen threshold each
#time and compare it with a value I picked by eye.

import cv2
import numpy as np

# --- Part 1: the dolphin image ---
img = cv2.imread("img.png")
#Converting the 3-channels dolphin into grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#Applying Otsu method to the gray dolphin
t_otsu, otsu = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)
print("Otsu chose:", t_otsu)

#Applying the binary thresholding into the gray dolphin
t_eye, by_eye = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)

# --- Part 2: My Day 13 noisy square ---
size = 100
sq = np.zeros((size, size), dtype=np.float32)
sq[30:70, 30:70] = 200
noisy = np.clip(sq + np.random.normal(0, 30, (size, size)), 0, 255).astype(np.uint8)

t_noisy, noisy_otsu = cv2.threshold(noisy, 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)
print("Otsu chose on the noisy square:", t_noisy)

# --- Part3: Show ---
row1 = np.hstack([gray, by_eye, otsu])
cv2.imshow("gray | 127 | Otsu", cv2.resize(row1, None, fx=0.5, fy=0.5))
row2 = np.hstack([noisy, noisy_otsu])
cv2.imshow("noisy | Otsu", cv2.resize(row2, None, fx=3, fy=3, interpolation=cv2.INTER_NEAREST))
cv2.waitKey(0)
cv2.destroyAllWindows()