import numpy as np
import matplotlib.pyplot as plt

# Generate a 2D array of random noise simulating pixel values (0 to 255)
# Shape: 100 rows by 100 columns
noise_image = np.random.randint(0, 256, size=(100, 100), dtype=np.uint8)

# Display the NumPy array as an image using Matplotlib
plt.imshow(noise_image, cmap='gray')
plt.title("Random Noise Simulation")
plt.colorbar()
plt.show()

