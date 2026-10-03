import numpy as np

# Define rotation angle in degrees and convert to radians
angle_deg = 30.0
angle_rad = np.radians(angle_deg)

# Calculate cosine and sine components
c, s = np.cos(angle_rad), np.sin(angle_rad)

# Construct the 2D rotation matrix R
R = np.array([[c, -s],
              [s,  c]], dtype=np.float32)

# Define a spatial pixel vector to rotate
v = np.array([10.0, 0.0], dtype=np.float32)

# Perform coordinate rotation
v_rotated = R @ v
print("Rotated vector:", v_rotated)
# Output: [8.660254 5.0]