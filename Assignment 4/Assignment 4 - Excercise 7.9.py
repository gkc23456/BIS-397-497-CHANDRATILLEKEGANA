# Assignment 4 - Exercise 7.9

import numpy as np

numbers = np.arange(1, 16).reshape(3, 5)

numbers

# a
numbers[2]

# b
numbers[:, 4]

# c
numbers[0:2]

# d
numbers[:, 2:5]

# e
numbers[1, 4]

# f
numbers[1:3, [0, 2, 4]]
