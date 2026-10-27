###DAY31: Practice day
##CHALLENGE2:load image→ resize half → flip horizontal → name as text bottom-left → save.

import cv2
img = cv2.imread("lena.png")
resized = cv2.resize(img,None,fx=0.5,fy=0.5)
flipped = cv2.flip(resized,1)
h, w = flipped.shape[:2]
cv2.putText(
    flipped,
    "Razak Sankara",
    (10, h - 10),
    cv2.FONT_HERSHEY_SIMPLEX,
    0.45,
    (0, 255, 255),
    1,
)
cv2.imshow("Razak Sankara",flipped)
cv2.waitKey(0)
cv2.imwrite("Razak Sankara.jpg",flipped)
cv2.destroyAllWindows()
