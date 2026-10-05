###DAY 18
##Practice 2
import cv2
cap = cv2.VideoCapture("video2.mp4")
total_frames = cap.get(cv2.CAP_PROP_FRAME_COUNT) #Counting the total number of frames
fps = cap.get(cv2.CAP_PROP_FPS)
print("Total frames:", total_frames)
print("FPS:", fps)

while True:
    ret,frame = cap.read()
    if ret == False:
        break;
    cv2.imshow("Video",frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()