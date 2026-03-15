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

#threeD dimentions 
arr4=np.array([[[1,2,3],[4,5,6],[7,8,9]],[[1,2,3],[4,5,6],[7,8,9]]])
print(arr4)

#multiple dimentions 
arr5=np.array([1,2,3,4,5],ndmin=4)
print(arr5.ndim)
print(arr5[0][1][3])


