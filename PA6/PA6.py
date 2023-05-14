# Deric Shaffer
# CS471 - PA6
# Due Date: April 9th, 2023

import threading as th
import time as t
import numpy as np

# obtain a value for n from the user
n = int(input("Enter a value for N: "))

# create an NxN matrix and fill it randomly with INTEGERS from 0 to 2^20
matrix = np.random.randint(0, 2**20, size=(n, n))

# calculate min, max, avg of all values w/o threading
print("\n-------- w/o Threading --------")
start1 = t.time()

# initialize min_val and max_val for comparisons in for loop
min_val = matrix[0][0]
max_val = matrix[0][0]

# sum variable for average
s = 0

# iterate over matrix
for i in range(n):
    for j in range(n):
        # update min_val if value is smaller
        if matrix[i][j] < min_val:
            min_val = matrix[i][j]
        
        # update max_val if value is larger
        if matrix [i][j] > max_val:
            max_val = matrix[i][j]
        
        # add value to sum
        s += matrix[i][j]

# calculate average
avg = s / (n*n)

# print out results
print("Min Value: " + str(min_val))
print("Max Value: " + str(max_val))
print("Average Value: " + str(avg))

stop1 = t.time()

print("Runtime: " + str((stop1 - start1) * 1000) + " milliseconds")


# calculate min, max, avg of all values w/ threading
print("\n-------- w/ Threading --------")
start2 = t.time()

# helper dictionary to store the values obtained from process_rows
results = {'min': [], 'max': [], 'avg': []}

# list to store threads
threads = []

def process_rows(r):
    min_val = np.min(r)
    results['min'].append(min_val)

    max_val =np.max(r)
    results['max'].append(max_val)

    avg = np.mean(r)
    results['avg'].append(avg)

    return min_val, max_val, avg

# create threads and append to list
for i in range(n):
    thread = th.Thread(target=process_rows, args=(matrix[i],))
    threads.append(thread)

    # start thread
    thread.start()

# wait for all threads to finish
for thread in threads:
    thread.join()

# determine min, max, and avg of entire matrix
print("Min Value: " + str(np.min(np.array(results['min']))))
print("Max Value: " + str(np.max(np.array(results['max']))))
print("Average Value: " + str(np.mean(np.array(results['avg']))))

stop2 = t.time()

print("Runtime: " + str((stop2 - start2) * 1000) + " milliseconds\n")