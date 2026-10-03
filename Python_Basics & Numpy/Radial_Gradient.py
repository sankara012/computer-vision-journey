import numpy as np
import matplotlib.pyplot as plt

# Generate a coordinate grid
x = np.linspace(-5, 5, 100)
y = np.linspace(-5, 5, 100)
xx, yy = np.meshgrid(x, y)

# Create a radial gradient pattern using Euclidean distance
radial_gradient = np.sqrt(xx**2 + yy**2)

# Display the synthetic radial gradient
plt.imshow(radial_gradient, cmap='viridis')
plt.title("Synthetic Radial Gradient")
plt.colorbar()
