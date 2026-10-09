### Day 20: SAVING VIDEO
## CHALLENGE: Record 5 seconds of webcam video and save it as .mp4
import cv2
import time

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Cannot open camera")
    exit()

width  = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps    = cap.get(cv2.CAP_PROP_FPS)
print("Camera reported FPS:", fps)

if fps == 0:
    fps = 20

fourcc = cv2.VideoWriter_fourcc(*'mp4v')
writer = cv2.VideoWriter("recording.mp4", fourcc, fps, (width, height))

frames_written = 0
start_time = time.time()

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    writer.write(frame)
    frames_written += 1
    cv2.imshow("Recording", frame)

    if cv2.waitKey(1) & 0xFF == ord('q') or time.time() - start_time > 5:
        break

elapsed = time.time() - start_time

cap.release()
writer.release()
cv2.destroyAllWindows()

print("Frames written:", frames_written)
print("Elapsed:", round(elapsed, 2), "seconds")
print("Actual FPS achieved:", round(frames_written / elapsed, 2))