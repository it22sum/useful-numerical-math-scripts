import numpy as np

def householder_transform(v):
    v = np.array(v)
    norm = np.linalg.norm(v)
    if norm == 0:
        raise ValueError("Nullvektor kann nicht für die Householder-Transformation verwendet werden.")

    # Richtung des Householder-Vektors
    e = np.zeros_like(v)
    e[0] = norm

    # Householder-Vektor
    u = (v - e) / np.linalg.norm(v - e)

    # Householder-Matrix
    H = np.eye(len(v)) - 2 * np.outer(u, u)

    return H

# Beispielvektor
v = [1, 2, 3]

H = householder_transform(v)
print("Householder-Matrix:\n", H)
