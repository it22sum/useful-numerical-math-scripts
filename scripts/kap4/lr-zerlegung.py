import numpy as np

def lu_decomposition(matrix):
    n = len(matrix)
    L = np.zeros((n, n))
    R = np.copy(matrix)

    for i in range(n):
        L[i, i] = 1
        for j in range(i+1, n):
            factor = R[j, i] / R[i, i]
            L[j, i] = factor
            R[j, i:] = R[j, i:] - factor * R[i, i:]

    return L, R

# Beispielmatrix
A = np.array([[1, 1, 1],
              [2, 2, 5],
              [4, 6, 8]])

L, R = lu_decomposition(A)
print("A:\n", A)
print("L:\n", L)
print("R:\n", R)
