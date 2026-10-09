import cv2

# Open primary camera (index 0) and secondary camera (index 1)
cap_primary = cv2.VideoCapture(0)
cap_secondary = cv2.VideoCapture(1)

while cap_primary.isOpened() and cap_secondary.isOpened():
    ret1, frame1 = cap_primary.read()
    ret2, frame2 = cap_secondary.read()

    if not ret1 or not ret2:
        break

    cv2.imshow('Primary Feed', frame1)
    cv2.imshow('Secondary Feed', frame2)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap_primary.release()
cap_secondary.release()
cv2.destroyAllWindows()