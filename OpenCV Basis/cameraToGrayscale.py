###Day 19:  WEBCAM BASICS
##CHALLENGE: display my webcam feed live, convert it to grayscale in real time
import cv2
"""Initialize capturing video from camera"""
cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("Cannot open camera")
    exit()
while cap.isOpened():
    ret,frame = cap.read()
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break
    """Converting frame to grayscale in real time"""
    gray_frame = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    cv2.imshow('Live Grayscale Feed',gray_frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

##Printing out the shape of the grayscale.
print("Shape:", gray_frame.shape)
"""Cleaning up and releasing hardware resources"""
cap.release()
cv2.destroyAllWindows()