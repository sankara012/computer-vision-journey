import numpy as np
arr = [[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20],[21,22,23,24,25]]
print(arr)
print("Convert into numpy array")
numpy_arr = np.array(arr)
print(numpy_arr)
#print the array shape
print(f"The array shape is: {numpy_arr.shape}")
print(f"The dimension of the array is: {numpy_arr.ndim}")
print(f"The type of data retained in the array is: {numpy_arr.dtype}")
