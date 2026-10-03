##Using the Pillow library
from PIL import Image
import numpy as np
img = Image.open("./test.jpg").convert("L")
img_array = np.array(img)
#current size
print(img_array.size)
print(img_array)
print(f"Shape: {img_array.shape}")
print(img_array.size)
# Resize the image
resized_array = np.resize(img_array,(200,200))
# Convert the resized array back to an image and save it
resized_array = Image.fromarray(resized_array)
resized_array.save('resized_array.jpg')
print(f"resized array: {resized_array}")
print(img_array.shape)
pixel_value = img_array[0,4]
print(f"pixel value at [0,]: {pixel_value}")
