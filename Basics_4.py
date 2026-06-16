import numpy as np

# fancy indexing in numpy

arr = np.array([10,20,30,40,50,60,70,80,90])
print(arr[[0,2,4,6,8]]) # fancy indexing with list of index
print(arr[[0,2,4,6,8]]*5) # fancy indexing with list of index and calculation

# fancy indexing in 2D array

arr = np.array([[10,20,30] , [40,50,60] , [70,80,90]])
print(arr[[0,2],[0,2]]) # fancy indexing with list of index in 2D array
print(arr[[0,2],[0,2]]*5) # fancy indexing with list of index in 2D array and calculation

# conditional selection in numpy

arr = np.array([5,7,11,18,30])
print(np.where(arr>10,arr,0)) # conditional selection with np.where() function

# sorting and ordering in numpy

arr = np.array([2,10,56,1,54])
print(np.sort(arr)) # sorting the array in ascending order

arr = np.array([2,10,56,1,54])
print(np.argsort(arr)) # gives the index of sorted array

# concatenation of arrays in numpy

arr1 = np.array([1,2,3])
arr2 = np.array([4,5,6])    
print(np.concatenate((arr1,arr2))) # concatenation of 1D arrays

# vertical and horizontal stacking of arrays in numpy

arr1 = np.array([[1,2,3] , [4,5,6]])
arr2 = np.array([[7,8,9] , [10,11,12]])

print(np.vstack((arr1,arr2))) # vertical stacking of 2D arrays

print(np.hstack((arr1,arr2))) # horizontal stacking of 2D arrays