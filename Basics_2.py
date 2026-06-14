import numpy as np

arr = [[1,2,3] , [4,5,6] , [7,8,9]]
arr = np.array(arr)

# shape of array , array_name.shapr

print(arr.shape)

# dimension of array , array_name.ndim

print(arr.ndim)

# number of element in array or size of array , array_name.size

print(arr.size)

# data type of array , array_name.dtype

print(arr.dtype)

# indexing and slicing of 1D array

arrey = np.array([10,20,30,40,50,60,70,80,90])
print(arrey[3]) # indexing
print(arrey[1:7:2]) # slicing [start:stop:step]

# indexing and slicing of 2D array

arry = np.array([[10,20,30] , [40,50,60] , [70,80,90]])
print(arry[0,0]) # indexing
print(arry[0:3:2,0:3:2]) # slicing of 2D array [row start:row end:step,column start:column end:step]

# boolean indexing

arey = np.array([1,2,3,4,5,6,7,8,9])
print(arey>5) # give output in the form of true and false

# reshaping the array using np.reshape(rows,columns) = 2D array , np.reshape(number of blocks,number of rows in block,number of columns in block)

arr = np.array([1,2,3,4,5,6,7,8])
reshape_2D_array = arr.reshape(2,4) # 2D array
print (reshape_2D_array)
reshape_3D_array = arr.reshape(2,2,2) # 3D array
print(reshape_3D_array)

# flattening 2D array into 1D array using flatten() function

arr = np.array([[1,2,3] , [4,5,6] , [7,8,9]])
one_D_array = arr.flatten()
print(one_D_array)