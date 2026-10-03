##2D rotation matrices
import numpy as np
angle_deg = 180.0
angle_rad = np.radians(angle_deg)
#cosine, sine components
C,S = np.cos(angle_rad),np.sin(angle_rad)
#construct the 2D rotation matrix R
R = np.array([[C, -S],
             [S, C]],dtype = np.float32
)

V = np.array([10.0,0.0],dtype=np.float32)
V_rotated = R @ V
print(f"Original vector:{V}")
print(f"Rotated vector:{V_rotated}")