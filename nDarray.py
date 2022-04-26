import numpy as np;
#1D array
array1 = np.array([1,2])
print(array1.shape)
print(array1.size)
print(array1.ndim)
print(array1.dtype)
print(type(array1))

#2D array
array2 = np.array([[1.,2.,3.],[4.,5.,6.]])
print(array2.shape)
print(array2.size)
print(array2.ndim)
print(array2.dtype)

#3D array
array3 = np.array([[[1,2,3],
[4,5,6],
[7,8,9]],
[[2,3,4],
[5,7,8],
[4,5,6]],
[[2,3,5],
[5,7,9],
[8,5,6]]])
print(array3.shape)
print(array3.size)
print(array3.ndim)
print(array3.dtype)
