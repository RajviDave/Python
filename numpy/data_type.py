import numpy as np

#you can explicitly mention the datatype
arr=np.array([1,0,1,0],dtype='i')

#astype function creates copy of existing array
new_arr=arr.astype('f')
arr1=arr.astype(bool)
print(arr1.dtype)
