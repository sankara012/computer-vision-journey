import numpy as np
import matplotlib.pyplot as plt
size = 255
y,x = np.ogrid[:size,:size]
center_y,center_x = size//2,size//2
radius = 50
mask = (x-center_x)**2 + (y-center_y)**2 <= radius**2
circle_image = mask.astype(np.uint8)*255
plt.imshow(circle_image,cmap='gray')
plt.title("Circle via distance formula")