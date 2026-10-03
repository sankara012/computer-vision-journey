###DAY 14
import cv2
import numpy as np
test = cv2.imread("img.png")
print(f"The image type is {type(test)}")
print(f"Shape is {test.shape}")
print(f"dtype is {test.dtype}")
pixel = test[280, 270]  # roughly center of the image
print("Raw pixel at (280, 270):", pixel)
print("That's just a NumPy array too:", type(pixel))