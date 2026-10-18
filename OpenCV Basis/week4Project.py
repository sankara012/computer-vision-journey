### DAY 28: REVIEW + MINI PROJECT
## MINI PROJECT: apply a 'random transform' each time you press a key — random rotation, random crop,random flip

import cv2
import random
img = cv2.imread("img.png")
def random_transform(src):
    h, w = src.shape[:2]
    out = src.copy()

    # 1) random rotation
    angle = random.uniform(-45, 45)
    M = cv2.getRotationMatrix2D((w // 2, h // 2), angle, 1.0)
    out = cv2.warpAffine(out, M, (w, h))

    # 2) random flip, about half of the time
    if random.random() < 0.5:
        out = cv2.flip(out, random.choice([-1, 0, 1]))

    # 3) random crop, then resize back
    ch = random.randint(int(0.6 * h), h)
    cw = random.randint(int(0.6 * w), w)
    y1 = random.randint(0, h - ch)
    x1 = random.randint(0, w - cw)
    out = out[y1:y1 + ch, x1:x1 + cw]
    return cv2.resize(out, (w, h))
while True:
    result = random_transform(img)
    cv2.imshow("Original", img)
    cv2.imshow("Random transform", result)

    key = cv2.waitKey(0) & 0xFF
    if key == ord('q'):
        break

cv2.destroyAllWindows()