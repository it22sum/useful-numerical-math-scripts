import numpy as np
# -*- coding: utf-8 -*-
"""
Created on Sat Nov  7 13:26:09 2020

Höhere Mathematik 1, Serie 8, Gerüst für Aufgabe 2

Description: calculates the QR factorization of A so that A = QR
Input Parameters: A: array, n*n matrix
Output Parameters: Q : n*n orthogonal matrix
                   R : n*n upper right triangular matrix
Remarks: none
Example: A = np.array([[1,2,-1],[4,-2,6],[3,1,0]])
        [Q,R]=Serie8_Aufg2(A)

@author: knaa
"""


def Serie8_Aufg2(A):
    import numpy as np

    A = np.copy(A)  # necessary to prevent changes in the original matrix A_in
    A = A.astype('float64')  # change to float

    n = np.shape(A)[0]

    if n != np.shape(A)[1]:
        raise Exception('Matrix is not square')

    Q = np.eye(n)
    R = A

    for j in np.arange(0, n - 1):
        a = np.copy(R[j:, j]).reshape(n - j, 1)
        e = np.eye(np.size(a))[:, 0].reshape(n - j, 1)
        length_a = np.linalg.norm(a)
        if a[0] >= 0:
            sig = 1
        else:
            sig = -1
        v = a + sig * length_a * e
        u = (1 / np.linalg.norm(v)) * v
        H = np.eye(np.size(a)) - (2 * u.dot(u.T))
        Qi = np.eye(n)
        Qi[j:, j:] = H
        R = Qi.dot(R)
        Q = Q.dot(Qi.T)

    return (Q, R)

A = np.array([
    [1, -2, 3],
    [-5, 4, 1],
    [2, -1, 3]
])


(Q, R) = Serie8_Aufg2(A)
(npQ, npR) = np.linalg.qr(A)
#print(npQ)
print(npR)

#print(Q)
print(R)