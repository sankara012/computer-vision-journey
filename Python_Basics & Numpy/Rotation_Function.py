import numpy as np


def rotate_point_2d(point, angle_degrees):
    # 1. Convert input degree angle to radians
    angle_rad = np.radians(angle_degrees)

    # 2. Compute trig components
    c = np.cos(angle_rad)
    s = np.sin(angle_rad)

    # 3. Assemble the rotation matrix
    R = np.array([[c, -s],
                  [s, c]], dtype=np.float32)

    # 4. Multiply matrix with our point array
    rotated_point = R @ point
    return rotated_point


# Test with our favorite unit vector!
vector = np.array([1.0, 0.0], dtype=np.float32)
result = rotate_point_2d(vector, 90.0)
print("Rotated coordinate:", result)
magnitude = np.linalg.norm(vector)
print("Magnitude:", magnitude)