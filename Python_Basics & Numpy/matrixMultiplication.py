import numpy as np
M = np.array([[2,1],[0,3]],dtype=np.uint8)
V = np.array([[10,20],[2,3]],dtype=np.uint8)
V_scaled_opt = M @ V
print(f"M: {M}")
print(f"V: {V}")
print(f"V_scaled_opt: {V_scaled_opt}")
V_scaled_dot = np.dot(M,V)
print(f"V_scaled_dot: {V_scaled_dot}")

#The dot product
a = np.array([2,1,4,5,5])
b = np.array([4,2,8,10,5])
c = np.dot(a,b)
print(f"a: {a}")
print(f"b: {b}")
print(f"The dot product gives: {c}")