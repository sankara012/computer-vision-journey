### DAY 21: REVIEW + MINI PROJECT
## CHALLENGE: Open webcam, press(s) to save a Snapshot(imwrite()), 'q' to quit.

import cv2
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Cannot open camera")
    exit()

count = 0

while True:
    ret, frame = cap.read()
    if not ret:
        break

    cv2.imshow("Snapshot Tool", frame)

    key = cv2.waitKey(1) & 0xFF

    if key == ord('q'):
        break
    elif key == ord('s'):
        filename = f"snapshot_{count}.png"
        cv2.imwrite(filename, frame)
        count += 1
        print("Saved", filename)

cap.release()
cv2.destroyAllWindows()