import numpy as np

#0D Array
arr = np.array(42)
print(arr.ndim,arr)

#1D Array
arr = np.array([1, 2, 3, 4, 5])
print(arr.ndim,arr)

#2D Array
arr = np.array([[1, 2, 3], [4, 5, 6]])
print(arr.ndim,arr) 

#3D Array
arr = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])
print(arr.ndim,arr) 

#Multi Dimension Array
arr = np.array([1, 2, 3, 4], ndmin=5)
print(arr.ndim,arr)
