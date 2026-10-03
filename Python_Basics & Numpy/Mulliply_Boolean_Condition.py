###Combining Multiple Boolean Conditions
import numpy as np

# Simulated row of pixel intensities
pixels = np.array([50, 120, 180, 240, 150], dtype=np.uint8)

# Create a mask for mid-tone pixels (between 100 and 200 inclusive)
mid_tone_mask = (pixels >= 100) & (pixels <= 200)

print("Mask:", mid_tone_mask)


print("Matching pixels:", pixels[mid_tone_mask])
