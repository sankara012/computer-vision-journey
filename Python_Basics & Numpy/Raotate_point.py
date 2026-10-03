##Day 10
import numpy as np
def rotate_point_2D(point,angle_degree):
  angle_rad = np.radians(angle_degree)
  C,S = np.cos(angle_rad),np.sin(angle_rad)
  R = np.array([
      [C, -S],
      [S, C]
  ], dtype=np.float32)
  rotated_point = R @ point
  return rotated_point
vector = np.array([1.0,0.0],dtype=np.float32)
result = rotate_point_2D(vector,90.0)
print(f"Rotated vector:{result}")