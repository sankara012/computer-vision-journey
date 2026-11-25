##DAY41:Practice Day: Live Color Mask
##Project:show the original feed and the masked feed side by side while holding a colored object in front of the camera.

#STEP BY STEP ALGORITHM
"""
1-Open the webcam, with the isOpened guard from Day 19.
2-In a while True loop, read a frame and break if ret is false.
3-Convert the frame to HSV.
4-Build a mask with cv2.inRange and your color range.
5-Cut the frame with cv2.bitwise_and(frame, frame, mask=mask).
6-Join the original and the masked frame with np.hstack.
7-Show it, quit on q, and release the camera at the end.

"""


import cv2
import numpy as np
cap = cv2.VideoCapture(0)                                                           #STEP1
if not cap.isOpened():
    print("Cannot open camera")
    exit()
while True:                                                                         #STEP2
    ret, frame = cap.read()
    if not ret:
        break
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)                                    #STEP3

    blue_mask = cv2.inRange(hsv, (101, 100, 60), (130, 255, 255))     #STEP4

    frame_cut = cv2.bitwise_and(frame, frame, mask=blue_mask)                       #STEP5

    row = np.hstack((frame, frame_cut))                                             #STEP6
    cv2.imshow("Original frame | Masked Frame", row)
    key = cv2.waitKey(1) & 0xFF
    if key == ord('q'):
        break
    elif key == ord('s'):
        cv2.imwrite("BlueMask.png", row)            # To save the blue mask frame
        print("Saved BlueMask.png")

cap.release()
cv2.destroyAllWindows()