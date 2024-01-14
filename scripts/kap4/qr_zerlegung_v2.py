import numpy as np

# Setzen der NumPy Druckoptionen für eine schönere Ausgabe
np.set_printoptions(precision=3, suppress=True)


def householder_transform(v):
    v = np.array(v, dtype=float)
    norm = np.linalg.norm(v)
    if norm == 0:
        raise ValueError("Nullvektor kann nicht für die Householder-Transformation verwendet werden.")

    e = np.zeros_like(v)
    e[0] = np.copysign(norm, v[0])
    u = (v - e) / np.linalg.norm(v - e)
    H = np.eye(len(v)) - 2 * np.outer(u, u)

    print("\nBerechnung der Householder-Transformation:")
    print(f"v = {v}")
    print(f"norm = {norm}")
    print(f"e = {e}")
    print(f"u = {u}")
    print(f"Householder-Matrix H = I - 2 * uu^T:\n{H}")

    return H


def qr_decomposition(A):
    m, n = A.shape
    Q = np.eye(m)

    for i in range(n - (m == n)):
        x = A[i:, i]
        H_i = np.eye(m)
        H_i[i:, i:] = householder_transform(x)

        # Anwendung der Householder-Transformation auf A für den aktuellen Schritt i
        A = np.dot(H_i, A)
        print(f"\nSchritt {i + 1}: Anwendung der Householder-Matrix auf A:")
        print(f"Transformierte Matrix A = H_i * A:\n{A}")

        # Akkumuliere die Householder-Matrizen, um Q zu berechnen
        Q = np.dot(Q, H_i)
        print(f"Update der orthogonalen Matrix Q = Q * H_i:\n{Q}")

    # Runde die Werte in A auf 0, wenn sie unter einer gewissen Toleranz liegen
    R = np.where(np.abs(A) < 1e-10, 0, A)
    return Q, R


# Beispielmatrix
A = np.array([[0,-4,2], [6, -3, -2], [8, 1, -1]], dtype=float)
print("Ursprüngliche Matrix A:\n", A)

Q, R = qr_decomposition(A)
print("Orthogonale Matrix Q:\n", Q )
print("Obere Dreiecksmatrix R:\n", R)
