import numpy as np

# broadcasting in numpy

arr = np.array([10,20,30,40,50])
print(arr*5)

# calculation on row but dimensions should be same

A = np.array([[10,20,30],[40,50,60]])
B = np.array([1,2,3])
print(A+B)

# argument functions in numpy

# sum of all element in array , np.sum(array_name)

arr = np.array([[1,2,3] , [4,5,6] , [7,8,9]])
print(np.sum(arr))

# mean of all element in array , np.mean(array_name)

print(np.mean(arr))

# minimum element in array , np.min(array_name)

print(np.min(arr))

# maximum element in array , np.max(array_name)

print(np.max(arr))

# standard deviation of all element in array , np.std(array_name)

print(np.std(arr))

# variance of all element in array , np.var(array_name)

print(np.var(arr))