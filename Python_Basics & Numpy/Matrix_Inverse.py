##Matrix Inverse
import numpy as np
A = np.array([[1, 2],
                   [4, 5]])
A_Inverse = np.linalg.inv(A)
print(A_Inverse)