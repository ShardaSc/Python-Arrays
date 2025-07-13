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

#### 16. How to add a border (filled with 0's) around an existing array?
arrrand = np.random.rand(4,4)
arrrand[1:1,1:1] =0
print(arrrand)


#### 17. What is the result of the following expression? (★☆☆)
'''python
0 * np.nan
np.nan == np.nan
np.inf > np.nan
np.nan - np.nan
np.nan in set([np.nan])
0.3 == 3 * 0.1
'''

False

#### 18. Create a 5x5 matrix with values 1,2,3,4 just below the diagonal (★☆☆)
# k=0 → main diagonal
#
# k=-1 → one below the diagonal
#
# k=1 → one above the diagonal

mat = np.diag([1, 2, 3, 4], k=-1)
print(mat)

#### 19. Create a 8x8 matrix and fill it with a checkerboard pattern (★☆☆)

checkerboard  = np.zeros((8,8),dtype=int)
checkerboard[1::2,::2] =1
checkerboard[::2,1::2] =1
print(checkerboard)

#### 20. Consider a (6,7,8) shape array, what is the index (x,y,z) of the 100th element? (★☆☆)

largestarr = np.zeros((6,7,8),dtype=int)
index = np.unravel_index(99,largestarr.shape)
print(index)

#### 21. Create a checkerboard 8x8 matrix using the tile function (★☆☆)
pattern = np.array([[1,0],[0,1]])
checkerboard1 = np.tile(pattern,(4,4))
print(checkerboard1)

#### 22. Normalize a 5x5 random matrix (★☆☆)
mat = np.random.rand(5,5)
nor_mat = (mat - np.min(mat)) / (np.max(mat) - np.min(mat))
print(nor_mat)

#### 23. Create a custom dtype that describes a color as four unsigned bytes (RGBA) (★☆☆)

colors = np.array([
    [255, 0, 0, 255],   # Red
    [0, 255, 0, 255],   # Green
    [0, 0, 255, 255]    # Blue
],dtype=np.uint8)
print(colors)

#### 24. Multiply a 5x3 matrix by a 3x2 matrix (real matrix product) (★☆☆)
farray = np.random.rand(5,3)
sarray = np.random.rand(3,2)
print(farray @ sarray) # we can also use np.dot(farray, sarray)

#### 25. Given a 1D array, negate all elements which are between 3 and 8, in place. (★☆☆)
negatearray = np.array([1,4,6,7,9,3,8])
negatearray[(negatearray > 3) & (negatearray < 8)] *=-1
print (negatearray)

#### 26. What is the output of the following script? (★☆☆)
'''python

print(sum(range(5),-1))
from numpy import *
print(sum(range(5),-1))
'''

print(sum(range(5),-1))
from numpy import *
print(sum(range(5),-1))


#### 27. Consider an integer vector Z, which of these expressions are legal? (★☆☆)
'''python
Z**Z
2 << Z >> 2
Z <- Z
1j*Z
Z/1/1
Z<Z>Z
'''
# The legal expressions are:
# Z**Z
# 2 << Z >> 2
# 1j * Z
# Z / 1 / 1


#### 28. What are the result of the following expressions? (★☆☆)
'''python
np.array(0) / np.array(0)
np.array(0) // np.array(0)
np.array([np.nan]).astype(int).astype(float)
'''

#### 30. How to find common values between two arrays? (★☆☆)
a = np.array([1, 2, 3, 4, 5])
b = np.array([4, 5, 6, 7, 8])

common = np.intersect1d(a, b)