# Deric Shaffer
# CS471 - PA3
# Due Date: March 5th, 2023

import time as t
import numpy as np
from scipy.linalg import lu

# scipy.linalg library has an lu function that does gaussian elimination
# takes in a matrix 'm' and returns a modified version of the inputted matrix
# no return statement due to it passing by reference
def gauss_np(m):
    p, l, u = lu(m)

# Test matrices consisting of random numbers from 1 to 50
matrix250 = np.random.randint(1, 51, size = (250, 251))
matrix500 = np.random.randint(1, 51, size = (500, 501))
matrix1000 = np.random.randint(1, 51, size = (1000, 1001))
matrix1500 = np.random.randint(1, 51, size = (1500, 1501))
matrix2000 = np.random.randint(1, 51, size = (2000, 2001))

# Test Cases
start = t.time()
matrix250 = gauss_np(matrix250)
stop = t.time()
print("Size = 250 Runtime: " + str(stop - start) + " seconds")

start = t.time()
matrix500 = gauss_np(matrix500)
stop = t.time()
print("Size = 500 Runtime: " + str(stop - start) + " seconds")

start = t.time()
matrix1000 = gauss_np(matrix1000)
stop = t.time()
print("Size = 1000 Runtime: " + str(stop - start) + " seconds")

start = t.time()
matrix1500 = gauss_np(matrix1500)
stop = t.time()
print("Size = 1500 Runtime: " + str(stop - start) + " seconds")

start = t.time()
matrix2000 = gauss_np(matrix2000)
stop = t.time()
print("Size = 2000 Runtime: " + str(stop - start) + " seconds")