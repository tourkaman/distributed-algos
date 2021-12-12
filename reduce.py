# mode = 'ring-allreduce'

# TODO Implement using actual separate processes using subprocessing
#      or multiprocessing libraries of python

# Processes or workers A-D,
# each with their own list of elements:

A = [17, 11,  1,  9]
B = [ 5, 13, 23, 14]
C = [12,  7,  2, 12]
D = [ 3,  6, 10,  8]

proc = [A, B, C, D]

m = len(proc)   # number of processes
# n = len(A)      # number of data elements (not needed right now)

steps = 2 * (m-1)

reduce = sum

# The algorithm has two major stages:
#   1. send elements around and store their sums  (for the first m-1 iteration steps)
#   2. send (sum of) elements around and copy their values  (for the second m-1 steps)

for k in range(steps):
    for p in range(m):

        p_prev = (p - 1) % m  # index of previous process
        i = (p_prev - k) % m  # bumping/rotating the indices one step

        if k < m - 1:
            # first stage: summing
            proc[p][i] = reduce([proc[p][i], proc[p_prev][i]])
        else:
            # second stage: copying
            proc[p][i] = proc[p_prev][i]

for p in proc:
    print(p)
