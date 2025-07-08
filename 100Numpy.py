# 100 numpy exercises

#1. Import the numpy package under the name `np` (★☆☆)

import numpy as np

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