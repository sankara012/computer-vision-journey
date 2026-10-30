###DAY35: Phase2 Wrap-up project
##PROJECT: Photo Booth App
##CHALLENGE: Opens webcam -> Press 'g' to toggle grayscale -> Press 'r' to rotate view 90° -> Press 's' to save snapshot with text overlay showing timestamp
# Press 'q' to quit

import cv2
from datetime import datetime

cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("Cannot open camera")
    exit()

gray_mode = False
rotation = 0
ROTATIONS = [None, cv2.ROTATE_90_CLOCKWISE, cv2.ROTATE_180, cv2.ROTATE_90_COUNTERCLOCKWISE]

while True:
    ret, frame = cap.read()
    if not ret:
        break

    view = frame
    if gray_mode:
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        view = cv2.cvtColor(gray, cv2.COLOR_GRAY2BGR)
    if ROTATIONS[rotation] is not None:
        view = cv2.rotate(view, ROTATIONS[rotation])

    cv2.imshow("Photo Booth", view)

    key = cv2.waitKey(1) & 0xFF
    if key == ord('q'):
        break
    elif key == ord('g'):
        gray_mode = not gray_mode
    elif key == ord('r'):
        #Use modular arithmetic to simplify the logic.The modulo operator, %, calculates the remainder after division.
        #Because of % 4, the result cycles through the integers 0, 1, 2, and 3.
        #The expression guarantees that the result stays within the valid index range for the four-element list which is ROTATIONS = [None, cv2.ROTATE_90_CLOCKWISE, cv2.ROTATE_180, cv2.ROTATE_90_COUNTERCLOCKWISE].
        rotation = (rotation + 1) % 4
    elif key == ord('s'):
        #Use (.copy)to add text to the image so that text can't become part of the live image displayed by the application.
        #view ─────> Current processed frame
        #snap ─────> Independent copy of that frame
        snap = view.copy()
        #Obtaining the timestamp
        now = datetime.now()                      #This obtains the current local date and time.
        label = now.strftime("%Y-%m-%d %H:%M:%S") #The strftime() method formats the datetime object as a string.
        h = snap.shape[0]
        cv2.putText(snap, label, (10, h - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 255), 2)
        filename = "photobooth_" + now.strftime("%Y%m%d_%H%M%S") + ".png"
        cv2.imwrite(filename, snap)
        print("Saved", filename)

cap.release()
cv2.destroyAllWindows()