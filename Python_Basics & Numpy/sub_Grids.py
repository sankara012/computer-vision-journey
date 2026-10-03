###Sub-Grids

import numpy as np
import matplotlib.pyplot as plt

# Create sample image data
image = np.random.randint(0, 256, size=(50, 50), dtype=np.uint8)

# Set up a 1x2 sub-grid layout
plt.figure(figsize=(8, 4))

# First panel: Original Image
plt.subplot(1, 2, 1)
plt.imshow(image, cmap='gray')
plt.title("Original Capture")

# Second panel: Simulated Filtered Image
plt.subplot(1, 2, 2)
plt.imshow(image[::-1, :], )
plt.title("Flipped Filter View")

plt.show()