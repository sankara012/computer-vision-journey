##DAY41:Mini Project: HSV Range Tuner
##Project: Build six sliders (H, S, V low and high) that update the mask live on the webcam feed.
#Goal: find the HSV range that isolates an object of your choice.
"""
On Day 41 I picked numbers, ran the script, looked, and edited the numbers again.
Today I'll drag six sliders and watch the mask update live
"""

import cv2
import numpy as np

def nothing(x):
    pass

cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("Cannot open camera")
    exit()

window = "HSV Tuner"
cv2.namedWindow(window)

cv2.createTrackbar("H low",  window, 101, 179, nothing)
cv2.createTrackbar("H high", window, 130, 179, nothing)
cv2.createTrackbar("S low",  window, 70, 255, nothing)
cv2.createTrackbar("S high", window, 255, 255, nothing)
cv2.createTrackbar("V low",  window, 60, 255, nothing)
cv2.createTrackbar("V high", window, 255, 255, nothing)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    h_lo = cv2.getTrackbarPos("H low", window)
    h_hi = cv2.getTrackbarPos("H high", window)
    s_lo = cv2.getTrackbarPos("S low", window)
    s_hi = cv2.getTrackbarPos("S high", window)
    v_lo = cv2.getTrackbarPos("V low", window)
    v_hi = cv2.getTrackbarPos("V high", window)

    mask = cv2.inRange(hsv, (h_lo, s_lo, v_lo), (h_hi, s_hi, v_hi))
    cut = cv2.bitwise_and(frame, frame, mask=mask)

    row = np.hstack([frame, cv2.cvtColor(mask, cv2.COLOR_GRAY2BGR), cut])
    cv2.imshow(window, cv2.resize(row, None, fx=0.5, fy=0.5))

    key = cv2.waitKey(1) & 0xFF
    if key == ord('q'):
        break
    elif key == ord('p'):
        print("lower =", (h_lo, s_lo, v_lo), " upper =", (h_hi, s_hi, v_hi))
    elif key == ord('s'):
        cv2.imwrite("MaskResult.png", row)
        print("Saved MaskResult.png")

cap.release()
cv2.destroyAllWindows()