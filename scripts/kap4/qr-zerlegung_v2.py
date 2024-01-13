import numpy as np


def householder_transform(v):
    v = np.array(v, dtype=float)
    norm = np.linalg.norm(v)
    if norm == 0:
        raise ValueError("Nullvektor kann nicht für die Householder-Transformation verwendet werden.")

    e = np.zeros_like(v)
    e[0] = np.copysign(norm, v[0])  # Wählt das Vorzeichen basierend auf v[0]
    u = (v - e) / np.linalg.norm(v - e)
    H = np.eye(len(v)) - 2 * np.outer(u, u)

    return H


def qr_decomposition(A):
    m, n = A.shape
    Q = np.eye(m)

    for i in range(n - (m == n)):
        H = np.eye(m)
        H[i:, i:] = householder_transform(A[i:, i])
        print(f"Schritt {i + 1} - Householder-Matrix H:\n", H)
        A = np.dot(H, A)
        print(f"Schritt {i + 1} - Transformierte Matrix A:\n", A)
        Q = np.dot(Q, H)

    return Q, A


# Beispielmatrix
A = np.array([[1, 2, -1], [4, -2, 6], [3, 1, 0]], dtype=float)
print("Ursprüngliche Matrix A:\n", A)

Q, R = qr_decomposition(A)
print("Orthogonale Matrix Q:\n", Q )
print("Obere Dreiecksmatrix R:\n", R)
