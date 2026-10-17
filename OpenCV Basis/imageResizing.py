import cv2
import numpy as np
img = cv2.imread("img.png")
print("original:", img.shape)

small = cv2.resize(img, (200,100))
half  = cv2.resize(img, None,fx=0.5,fy=0.5)
big   = cv2.resize(img, None, fx=2, fy=2, interpolation=cv2.INTER_NEAREST)
print("small:", small.shape)
print("half: ", half.shape)
print("big:  ", big.shape)

crop = img[130:150, 230:250]
print("crop: ", crop.shape)
near = cv2.resize(crop, None, fx=10, fy=10, interpolation=cv2.INTER_NEAREST)
print("near: ", near.shape)
lin = cv2.resize(crop, None, fx=10, fy=10, interpolation=cv2.INTER_LINEAR)
print("lin: ", lin.shape)
cub = cv2.resize(crop, None, fx=10, fy=10, interpolation=cv2.INTER_CUBIC)
print("cub: ", cub.shape)
area = cv2.resize(crop, None, fx=10, fy=10, interpolation=cv2.INTER_AREA)
print("area: ", area.shape)
row = np.hstack([near, lin, cub, area])
print("row: ", row.shape)

cv2.imshow("NEAREST | LINEAR | CUBIC | AREA", row)
cv2.waitKey(0)
cv2.destroyAllWindows()