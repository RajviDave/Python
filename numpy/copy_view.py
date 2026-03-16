import numpy as np

arr=[1,2,3,4,5]
arr=np.array(arr)

x=arr.copy()
y=arr.view()

arr[0]=4
y[1]=8

print(x)
print(y)
print(arr)