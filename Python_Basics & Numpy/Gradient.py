##Day 12
#Gradient
import numpy as np
width,height = 256,256
gradient_x = np.tile(np.arange(width,dtype=np.uint8),(height,1))
print(gradient_x)