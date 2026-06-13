import numpy as np

# creating array using np.array()

l = [10,20,30,40,50]
array = np.array(l)
print(array)

# creating 2D array using np.array()

a = [ [1,2,3] , [4,5,6] , [7,8,9] ]
two_D_array = np.array(a)
print(two_D_array)

# create a zeros array of given element np.zeros()

zero = np.zeros(4)
print(zero)

# creating a zeros 2D array using np.zero([rows,columns])

zero_2D_array = np.zeros([3,4])
print(zero_2D_array)

# creating a ones array of given element using np.ones()

one = np.ones(4)
print(one)

# creating a ones 2D array using np.ones([rows,columns])

one_2D_array = np.ones([3,4])
print(one_2D_array)

# creating a array of specific element of specific length np.full(length,element)

full = np.full(5,1)
print(full)

# creating 2D array of specific element np.full([rows,columns],element)

full_2D_array = np.full([3,4],7)
print(full_2D_array)

# creating array using np.arang(start,stop,step) sopt value not include

arrange = np.arange(2,11,2)
print(arrange)

# create a array containing a specified number of evenly spaced values between two endpoints np.linspace(start,stop,difference)

space = np.linspace(1,10,10)
print(space)

# creating 2D identity array using np.eye()

identity = np.eye(3)
print(identity)

# creating a 2D array of random values np.random.randint(start,stop,(rows,columns))

random_2D_array = np.random.randint(1,20,(3,3))
print(random_2D_array)