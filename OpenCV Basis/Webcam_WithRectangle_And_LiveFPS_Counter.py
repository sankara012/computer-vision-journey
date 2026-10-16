#### DAY 21: COMBINING DRAWING + WEBCAM
## CHALLENGE:  display webcam feed with a rectangle drawn in the center and live FPS counter as text

import cv2
import time
cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("Cannot open camera")
    exit()
prev_time = time.time()
while True:
    ret, frame = cap.read()
    if not ret:
        break
    h, w = frame.shape[:2]
    cx, cy = w // 2, h // 2
    cv2.rectangle(frame, (cx - 100, cy - 75), (cx + 100, cy + 75), (0, 255, 0), 2)
    now = time.time()
    fps = 1 / (now - prev_time)
    prev_time = now
    cv2.putText(frame, f"FPS: {fps:.1f}", (10, 30),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 255), 2)

    cv2.imshow("Webcam live feed with a centered rectangle and live FPS counter", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()