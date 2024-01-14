import numpy as np

def lu_decomposition(matrix):
    n = len(matrix)
    L = np.zeros((n, n))
    R = np.copy(matrix)

    for i in range(n):
        L[i, i] = 1
        for j in range(i+1, n):
            factor = R[j, i] / R[i, i]  # Berechnen des Faktors für die L-Matrix
            L[j, i] = factor  # Speichern des Faktors in der L-Matrix
            R[j, i:] = R[j, i:] - factor * R[i, i:]  # Aktualisieren der R-Matrix
            print(f"\nSchritt {i+1}.{j-i}:")
            print(f"Multipliziere Zeile {i+1} mit {factor} und subtrahiere von Zeile {j+1}")
            print(f"Update L-Matrix:\n{L}")
            print(f"Update R-Matrix:\n{R}")

    return L, R

# Beispielmatrix
A = np.array([[1, 2, 4],
              [2, 3, 8],
              [-1, -3, -1]])

print("Ursprüngliche Matrix A:\n", A)
L, R = lu_decomposition(A)
print("\nEndgültige L-Matrix:\n", L)
print("Endgültige R-Matrix:\n", R)
