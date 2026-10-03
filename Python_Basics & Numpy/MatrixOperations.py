import numpy as np

# 1. Identity Matrix
I = np.eye(2, dtype=np.float32)
print("Identity matrix:\n", I)
# 2. Transpose a coordinate matrix
A = np.array([[3.0, 1.0],
              [2.0, 4.0]], dtype=np.float32)
print("matrix A:\n", A)
A_transpose = A.T
print("Transposed matrix A:\n", A_transpose)
# 3. Determinant to check invertibility
det_A = np.linalg.det(A)
print("Determinant of A:", det_A) # Output: 10.0 (Non-zero, so safe to invert!)

# 4. Matrix Inverse to reverse spatial transformations
A_inverse = np.linalg.inv(A)
print("Inverse matrix:\n", A_inverse)