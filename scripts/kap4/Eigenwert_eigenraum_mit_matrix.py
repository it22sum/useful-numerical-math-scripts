import sympy as sp

def calculate_eigenvalues_and_eigenspaces(matrix):
    # Berechnen der Eigenwerte und Eigenvektoren
    eigenvectors = matrix.eigenvects()

    print("Eigenwerte und zugehörige Eigenräume:")
    for eigval, _, eigvecs in eigenvectors:
        print(f"Eigenwert: {eigval}")
        for vec in eigvecs:
            print(f"Eigenraum: {{x = a * {vec.T}; a in R}}\n")

# Beispielmatrix - ersetzen Sie diese Matrix durch Ihre eigene Matrix
A = sp.Matrix([[10, 9], [17, 5]])

# Berechnung der Eigenwerte und Eigenräume
calculate_eigenvalues_and_eigenspaces(A)

