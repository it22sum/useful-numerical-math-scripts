import numpy as np


def matrix_multiply(A, B):
    return np.dot(A, B)

def add_matrices(A, B):
    return np.add(A, B)

def subtract_matrices(A, B):
    return np.subtract(A, B)

def divide_matrices(A, B):
    B_inv = np.linalg.inv(B)
    return np.dot(A, B_inv)

def traverse_matrix_rowwise(matrix):
    for row in matrix:
        for element in row:
            print(element, end=' ')
        print()  # Neue Zeile nach jeder Zeile der Matrix

def traverse_matrix_columnwise(matrix):
    rows, cols = matrix.shape
    for col in range(cols):
        for row in range(rows):
            print(matrix[row, col], end=' ')
        print()  # Neue Zeile nach jeder Spalte der Matrix

# Beispielmatrizen
A = np.array([[1, 0, 0], [0, 1, 0], [0, 0, 1]])
B = np.array([[1, 2, 3], [2, 4, 6], [3, 6, 9]])

# Matrixmultiplikation
C = matrix_multiply(A, B)
print("Ergebnis der Matrixmultiplikation:\n", C)

C = add_matrices(A, B)
print("Ergebnis der Matrixaddition:\n", C)

C = subtract_matrices(A, B)
print("Ergebnis der Matrixsubtraktion:\n", C)

print("Zeilenweise Traversierung für Matrix A:")
traverse_matrix_rowwise(A)

print("Zeilenweise Traversierung für Matrix B:")
traverse_matrix_rowwise(B)

print("Spaltenweise Traversierung für Matrix A:")
traverse_matrix_columnwise(A)

print("Spaltenweise Traversierung für Matrix B:")
traverse_matrix_columnwise(B)

if np.linalg.det(B) != 0:
    # Matrixdivision
    C = divide_matrices(A, B)
    print("Ergebnis der Matrixdivision (A * B^-1):\n", C)
else:
    print("Matrix B ist nicht invertierbar.")