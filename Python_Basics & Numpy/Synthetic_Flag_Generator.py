import cv2
import numpy as np
#3D NumPy array of shape (100, 100, 3)
canvas = np.zeros((100,100,3),dtype=np.uint8)
canvas[:,:,0] = 255
##Overlaying the Red Square 50-50 top left
canvas[0:50,0:50] = [ 0, 0,255]
#Printing the shape and data type and dimension
print(canvas.shape,canvas.dtype,canvas.ndim)

# save and show
cv2.imwrite("flag_check.png", canvas)
cv2.imshow("Flag Check", canvas)
cv2.waitKey(0)
cv2.destroyAllWindows()


