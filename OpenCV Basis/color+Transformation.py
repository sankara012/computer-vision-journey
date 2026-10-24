####    WEEK5: CONSOLIDATION & BRIDGE TO IMAGE PROCESSING
### DAY 29: COMBINE COLOR + TRANSFORM
##  CHALLENGE:  load an image, convert to HSV, extract one channel (e.g. Hue), resize, display

import cv2
img = cv2.imread('cat.png')
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# Extract saturation channel
s_channel = hsv[:, :, 1]

# Resize the saturation channel
resized_saturation = cv2.resize(s_channel, (200, 200), interpolation=cv2.INTER_LINEAR)

cv2.imshow("Original image", img)
cv2.imshow("Saturation Channel", s_channel)
cv2.imshow('Resized Saturation Channel', resized_saturation)
cv2.waitKey(0)
cv2.destroyAllWindows()