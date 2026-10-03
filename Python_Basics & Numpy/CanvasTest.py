import numpy as np
from PIL import Image
canvas = np.zeros((100,100,3),dtype=np.uint8)
canvas[:,:,2] = 255
canvas[0:50,0:50] = [255,0,0]
canvas[50:100,0:50] = [0,0,0]
canvas[0:100,50:100] = [0,50,0]

img = Image.fromarray(canvas)
img.save("test.png")
img.show()
print(canvas.ndim,canvas.shape,canvas.dtype)
canvas_masked = canvas >= 30
##Boolean Masking
#print(canvas_masked)
##Integer array indexing
rows_extracted = canvas[[0,2,4],:]
print(rows_extracted)