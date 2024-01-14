import sympy as sp

def lu_decomposition(matrix):
    n = matrix.shape[0]
    L = sp.zeros(n, n)
    R = matrix.copy()

    for i in range(n):
        L[i, i] = 1
        for j in range(i + 1, n):
            factor = R[j, i] / R[i, i]
            L[j, i] = factor
            R[j, i:] = R[j, i:] - factor * R[i, i:]

            print(f"Schritt {i + 1}, Subschritt {j - i} der LR-Zerlegung:")
            print("L:\n", L)
            print("R:\n", R)
            print()

    return L, R

def forward_substitution(L, b):
    n = L.shape[0]
    y = sp.zeros(n, 1)
    for i in range(n):
        y[i] = b[i] - sum(L[i, j] * y[j] for j in range(i))
        print(f"Vorwärtseinsetzen Schritt {i + 1}:")
        print("y:\n", y)
        print()

    return y

def backward_substitution(R, y):
    n = R.shape[0]
    x = sp.zeros(n, 1)
    for i in range(n - 1, -1, -1):
        x[i] = (y[i] - sum(R[i, j] * x[j] for j in range(i + 1, n))) / R[i, i]
        print(f"Rückwärtseinsetzen Schritt {n - i}:")
        print("x:\n", x)
        print()

    return x

# Definiere eine invertierbare Matrix A und den Vektor b
A = sp.Matrix([[1, 2, 3],
               [4, 5, 6],
               [7, 8, 10]])
b = sp.Matrix([1, 2, 3])

# LR-Zerlegung
L, R = lu_decomposition(A)

# Löse Ly = b
y = forward_substitution(L, b)

# Löse Rx = y
x = backward_substitution(R, y)

print("Finale Lösung x:\n", x)
