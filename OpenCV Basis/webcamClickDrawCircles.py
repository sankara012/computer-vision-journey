#### WEEK5(PHASE2) ####
### DAY 30: REAL-TIME DRAWING APP
## MINI PROJECT: clicking on the webcam window draws a circle at that point (cv2.setMouseCallback())

import cv2

# Store click points here. Each webcam frame is a NEW image, so drawing
# only inside the callback would disappear on the next cap.read().
circles = []


def on_mouse(event, x, y, flags, param):
    # OpenCV calls this function for every mouse event on the named window.
    if event == cv2.EVENT_LBUTTONDOWN:
        circles.append((x, y))


cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("Cannot open camera")
    exit()

window_name = "Click to draw circles (c=clear, q=quit)"
cv2.namedWindow(window_name)
cv2.setMouseCallback(window_name, on_mouse)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    for (cx, cy) in circles:
        cv2.circle(frame, (cx, cy), 20, (0, 255, 0), 2)

    cv2.putText(
        frame,
        "Left click: draw  |  c: clear  |  q: quit",
        (10, 30),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.6,
        (0, 255, 255),
        2,
    )

    cv2.imshow(window_name, frame)

    key = cv2.waitKey(1) & 0xFF
    if key == ord("q"):
        break
    if key == ord("c"):
        circles.clear()

cap.release()
cv2.destroyAllWindows()
