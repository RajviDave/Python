import numpy as np

#conversion
array=(1,2,3,4,5)
print(type(array))

array=np.array([1,2,3,4,5])
print(type(array))

#dimentions in array

#zero dimention
arr1=np.array(30)
print(arr1.ndim)

#one dimention
arr2=np.array([1,2,3,4,5])
print(arr2.ndim)

#two dimentions
arr3=np.array([[1,2,3],[4,5,6]])
print(arr3.ndim)
print(arr3.shape)
