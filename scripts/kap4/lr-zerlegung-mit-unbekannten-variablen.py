import sympy as sp

def lu_decomposition(matrix):
    n = matrix.shape[0]  # Anzahl der Zeilen
    L = sp.zeros(n, n)
    R = matrix.copy()

    for i in range(n):
        L[i, i] = 1
        for j in range(i + 1, n):
            factor = R[j, i] / R[i, i]
            L[j, i] = factor
            R[j, i:] = R[j, i:] - factor * R[i, i:]

            print(f"Schritt {i + 1}, Subschritt {j - i}:")
            print("L:\n", L)
            print("R:\n", R)
            print()

    return L, R

# Definiere die unbekannte Variable ε
epsilon = sp.symbols('epsilon')

# Beispielmatrix mit ε
A = sp.Matrix([[1, 1, 1],
               [2, 2 + epsilon, 5],
               [4, 6, 8]])

L, R = lu_decomposition(A)
print("Finale LR-Zerlegung:")
print("L:\n", L)
print("R:\n", R)
