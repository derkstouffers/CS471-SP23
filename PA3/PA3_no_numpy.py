# Deric Shaffer
# CS471 - PA3
# Due Date: March 5th, 2023

import time as t
import random

# in: coefficient matrix 'm' and right-most vector 'b'
# out: solution vector 'res'
def gauss_reg(m, b):
    # iterate over the rows of the matrix
    for i in range(len(m)):
        for j in range(i + 1, len(m)):
            # determine factor to multiply to current row and eliminate elements
            factor = m[j][i] / m[i][i]
            for k in range(i + 1, len(m)):
                # subtracts element by the (factor * element before it in row)
                m[j][k] -= factor * m[i][k]
            
            # update element in rightmost
            b[j] -= factor * b[i]

    # returned result matrix
    res = [0] * len(m)

    # Backward elimination
    for i in range(len(m) - 1, -1, -1):
        res[i] = b[i] / float(m[i][i])
        for j in range(i):
            b[j] -= m[j][i] * res[i]

    return res

# variables
matrix = []
b = [] # rightmost vector

# populate matrix with random integers w/o numpy
for i in range(250):
    row = []
    for j in range(251):
        row.append(random.randint(1, 26))  # generate random integer between 1 and 25
    matrix.append(row)

# populate rightmost vector
for i in range(250):
    b.append(random.randint(1, 26))


start = t.time()
gauss_reg(matrix, b)
stop = t.time()
print("Size 250 Runtime: " + str(stop - start) + " seconds")

# update variables
matrix = []
b = [] # rightmost vector

# populate matrix with random integers w/o numpy
for i in range(500):
    row = []
    for j in range(501):
        row.append(random.randint(1, 26))  # generate random integer between 1 and 25
    matrix.append(row)

# populate rightmost vector
for i in range(500):
    b.append(random.randint(1, 26))


start = t.time()
gauss_reg(matrix, b)
stop = t.time()
print("Size 500 Runtime: " + str(stop - start) + " seconds")

# update variables
matrix = []
b = [] # rightmost vector

# populate matrix with random integers w/o numpy
for i in range(1000):
    row = []
    for j in range(1001):
        row.append(random.randint(1, 26))  # generate random integer between 1 and 25
    matrix.append(row)

# populate rightmost vector
for i in range(1000):
    b.append(random.randint(1, 26))


start = t.time()
gauss_reg(matrix, b)
stop = t.time()
print("Size 1000 Runtime: " + str(stop - start) + " seconds")

# update variables
matrix = []
b = [] # rightmost vector

# populate matrix with random integers w/o numpy
for i in range(1500):
    row = []
    for j in range(1501):
        row.append(random.randint(1, 26))  # generate random integer between 1 and 25
    matrix.append(row)

# populate rightmost vector
for i in range(1500):
    b.append(random.randint(1, 26))


start = t.time()
gauss_reg(matrix, b)
stop = t.time()
print("Size 1500 Runtime: " + str(stop - start) + " seconds")

# update variables
matrix = []
b = [] # rightmost vector

# populate matrix with random integers w/o numpy
for i in range(2000):
    row = []
    for j in range(2001):
        row.append(random.randint(1, 26))  # generate random integer between 1 and 25
    matrix.append(row)

# populate rightmost vector
for i in range(2000):
    b.append(random.randint(1, 26))


start = t.time()
gauss_reg(matrix, b)
stop = t.time()
print("Size 2000 Runtime: " + str(stop - start) + " seconds")