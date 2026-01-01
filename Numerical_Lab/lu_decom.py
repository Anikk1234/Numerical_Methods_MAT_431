#with Library:

# import numpy as np
# import scipy.linalg as la
#
# n=3
# A=np.random.randint(1,10,(n,n))
# print(f"Random matrix: {A}")
#
# p,l,u=la.lu(A)
#
# print(f"Lower triangular matrix: {l}")
# print(f"Upper triangular matrix: {u}")
#
# print("Verification of LU decomposition")
# print(p@l@u)
#


#without library:


import random


def lu_decomposition_manual(matrix):
    n = len(matrix)

    L = [[0.0] * n for _ in range(n)]
    U = [[0.0] * n for _ in range(n)]

    for i in range(n):
        # Upper Triangular
        for k in range(i, n):
            sum_val = 0
            for j in range(i):
                sum_val += (L[i][j] * U[j][k])
            U[i][k] = matrix[i][k] - sum_val

        for k in range(i, n):
            if i == k:
                L[i][i] = 1.0
            else:
                sum_val = 0
                for j in range(i):
                    sum_val += (L[k][j] * U[j][i])
                L[k][i] = (matrix[k][i] - sum_val) / U[i][i]

    return L, U





n = 3
A = [[random.randint(1, 9) for _ in range(n)] for _ in range(n)]

print("Random Matrix A:")
for row in A:
    print(row)

L_matrix, U_matrix = lu_decomposition_manual(A)

print("\nLower Triangular (L):")
for row in L_matrix:
    print([round(elem, 2) for elem in row])

print("\nUpper Triangular (U):")
for row in U_matrix:
    print([round(elem, 2) for elem in row])