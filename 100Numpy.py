# # 100 numpy exercises

# #1. Import the numpy package under the name `np` (★☆☆)

import numpy as np
#
#2. Print the numpy version and the configuration (★☆☆)
print(np.__version__)


#3. Create a null vector of size 10 (★☆☆)
print(np.zeros(10))

#4. How to find the memory size of any array (★☆☆)

arr = np.zeros(10)
print(arr.nbytes)

#5. How to get the documentation of the numpy add function from the command line? (★☆☆)
help(np.add)

#### 6. Create a null vector of size 10 but the fifth value which is 1 (★☆☆)
arr1 = np.zeros(10)
arr1[4] = 1
print(arr1)

#### 7. Create a vector with values ranging from 10 to 49 (★☆☆)
varr = np.arange(10,50)
print(varr)

#### 8. Reverse a vector (first element becomes last) (★☆☆)
print(varr[::-1])

#### 9. Create a 3x3 matrix with values ranging from 0 to 8 (★☆☆)
matrix = np.arange(9).reshape(3,3)
print(matrix)

#### 10. Find indices of non-zero elements from [1,2,0,0,4,0] (★☆☆)
nonzero1 = np.array([1,2,0,0,4,0])
indices = np.where(nonzero1 != 0)
print(indices[0])

#### 11. Create a 3x3 identity matrix (★☆☆)
iden = np.identity(3)
print(iden)

#### 12. Create a 3x3x3 array with random values (★☆☆)
randommat = np.random.rand(3,3,3)
print(randommat)

#### 13. Create a 10x10 array with random values and find the minimum and maximum values (★☆☆)
tenvalues = np.random.rand(10,10)
print(tenvalues,tenvalues.min(),tenvalues.max())

#### 14. Create a random vector of size 30 and find the mean value (★☆☆)
ranvector = np.random.random(30)
print(ranvector.mean())

#### 15. Create a 2d array with 1 on the border and 0 inside (★☆☆)
arr2 = np.ones((5,5),dtype=int)
arr2[1:-1,1:-1] = 0
print(arr2)