# mode = 'ring-allreduce'

# TODO Implement using actual separate processes using subprocessing
#      or multiprocessing libraries of python

# A = [1, 2, 3, 4]
# B = [1, 2, 3, 4]
# C = [1, 2, 3, 4]
# D = [1, 2, 3, 4]
# S = [4, 8, 12, 16]

A = [17, 11, 1, 9]
B = [5, 13, 23, 14]
C = [12, 7, 2, 12]
D = [3, 6, 10, 8]


proc = [A, B, C, D]

m = len(proc)   # number of processes
n = len(A)      # number of data elements

reduce = sum


# We are going to work per-data-element,
# as opposed to per-worker-available. ie
# we're going to loop through the data elements,
# and update each process accordingly. as opposed
# to the other way around.

# for i in range(n):
#     for p in range(m):
#         # i_prev = ... % n ?
#         p_prev = (p - 1) % m
#         proc[p][i] = reduce([proc[p][i], proc[p_prev][i]])




# or maybe not... maybe the thing should be based on processes instead?

# because the way you did it, only process C ends up with the correct
# results! you should be moving the i variable also forward by one step
# from process p to the next. and not just have a fixed i and then iterate
# through all the p's.


# for p in range(m):
#     # i_prev = ... % n ?
#     p_prev = (p - 1) % m
#     proc[p][p] = reduce([proc[p][p], proc[p_prev][p]])
# 
# print(A)
# print(B)
# print(C)
# print(D)




print('At the beginning')
print(A)
print(B)
print(C)
print(D)

A[3] = A[3] + D[3]
B[0] = B[0] + A[0]
C[1] = C[1] + B[1]
D[2] = D[2] + C[2]

print('\nAfter step 1')
print(A)
print(B)
print(C)
print(D)

A[2] = A[2] + D[2]
B[3] = B[3] + A[3]
C[0] = C[0] + B[0]
D[1] = D[1] + C[1]

print('\nAfter step 2')
print(A)
print(B)
print(C)
print(D)

A[1] = A[1] + D[1]
B[2] = B[2] + A[2]
C[3] = C[3] + B[3]
D[0] = D[0] + C[0]

print('\nAfter step 3')
print(A)
print(B)
print(C)
print(D)

# The fourth one and onward we just copy, instead of reducing
A[0] = D[0]
B[1] = A[1]
C[2] = B[2]
D[3] = C[3]

print('\nAfter step 4')
print(A)
print(B)
print(C)
print(D)

A[3] = D[3]
B[0] = A[0]
C[1] = B[1]
D[2] = C[2]

print('\nAfter step 5')
print(A)
print(B)
print(C)
print(D)

A[2] = D[2]
B[3] = A[3]
C[0] = B[0]
D[1] = C[1]

print('\nAfter step 6')
print(A)
print(B)
print(C)
print(D)

A[1] = D[1]
B[2] = A[2]
C[3] = B[3]
D[0] = C[0]

print('\nAfter step 7')
print(A)
print(B)
print(C)
print(D)


