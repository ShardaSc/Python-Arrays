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