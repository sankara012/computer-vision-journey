### DAY 18
##Practice1

import cv2

cap = cv2.VideoCapture("video.mp4")

while True:
    ret, frame = cap.read()

    if not ret:
        break  # <-- stop looping, no more valid frames

    cv2.imshow("Video Frame", frame)  # <-- only reached if ret was True

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()