###DAY31: Practice day
##CHALLENGE3: Webcam -> convert to HSV -> draw a circle in the center -> display

import cv2
cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("Cannot open camera")
    exit()
while True:
    ret, frame = cap.read()
    if not ret:
        break
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    h,w = hsv.shape[:2]
    cx,cy = int(w/2), int(h/2)
    cv2.circle(hsv, (cx,cy), 40, (255,0,0), 3)
    cv2.imshow('hsv live frame feed',hsv)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cv2.imwrite("hsv.jpg",hsv)
cap.release()
cv2.destroyAllWindows()