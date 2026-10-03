##Day 12
#Checkerboard
import numpy as np
import matplotlib.pyplot as plt
block_size = 32
grid_size = 8

# Create a small checker pattern (0s and 1s) for the grid_size
rows_small, cols_small = np.indices((grid_size, grid_size))
small_checker_pattern = ((rows_small + cols_small) % 2)

# Use kron to expand the small pattern into the full checkerboard
checkerboard = np.kron(small_checker_pattern, np.ones((block_size, block_size))).astype(np.uint8) * 255

plt.imshow(checkerboard,cmap='gray')
plt.title("Checkerboard")