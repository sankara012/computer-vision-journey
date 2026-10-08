import cv2

cap = cv2.VideoCapture("video2.mp4")

fps = cap.get(cv2.CAP_PROP_FPS)
delay = int(1000 / fps)          # ms per frame, about 41 at 24 FPS
total_frames = cap.get(cv2.CAP_PROP_FRAME_COUNT)
fps = cap.get(cv2.CAP_PROP_FPS)
width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)

print("Total frames:", total_frames)
print("FPS:", fps)
print("Resolution:", width, "x", height)
while True:
    ret, frame = cap.read()
    if not ret:
        break

    frame_small = cv2.resize(frame, None, fx=0.5, fy=0.5)
    cv2.imshow("Video Frame", frame_small)

    if cv2.waitKey(delay) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()