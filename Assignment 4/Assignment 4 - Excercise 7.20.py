# Assignment 4 - Exercise 7.20

# List Avg. Execution Time
import random

%timeit rolls_list = \
   [random.randrange(1, 2) for i in range(0, 1)]
   
%timeit rolls_list = \
   [random.randrange(1, 2) for i in range(0, 10)]

%timeit rolls_list = \
   [random.randrange(1, 2) for i in range(0, 100)]
   
%timeit rolls_list = \
   [random.randrange(1, 2) for i in range(0, 1000)]
   
%timeit rolls_list = \
   [random.randrange(1, 2) for i in range(0, 10000)]
   
%timeit rolls_list = \
   [random.randrange(1, 2) for i in range(0, 100000)]

%timeit rolls_list = \
   [random.randrange(1, 2) for i in range(0, 1000000)]
   
   
# Array Avg. Execution Time  
import numpy as np

%timeit -n1000000 -r7 rolls_array = np.random.randint(1, 2, 1)

%timeit -n100000 -r7 rolls_array = np.random.randint(1, 2, 10)

%timeit -n10000 -r7 rolls_array = np.random.randint(1, 2, 100)

%timeit -n1000 -r7 rolls_array = np.random.randint(1, 2, 1000)

%timeit -n100 -r7 rolls_array = np.random.randint(1, 2, 10000)

%timeit -n10 -r7 rolls_array = np.random.randint(1, 2, 100000)

%timeit -n1 -r7 rolls_array = np.random.randint(1, 2, 1000000)
