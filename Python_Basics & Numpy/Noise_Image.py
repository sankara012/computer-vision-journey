##Noise image with defaults colors
import numpy as np
import matplotlib.pyplot as plt
noise_img = np.random.randint(0,256,size=(100,100),dtype=np.uint8)
plt.imshow(noise_img)
plt.title("Random noise simulation")
plt.colorbar()
plt.show

