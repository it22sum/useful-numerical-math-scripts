import numpy as np
import matplotlib.pyplot as plt



A = np.array([
    [2,5],
    [-1,-2],
])

eigenvalues, eigenvectors = np.linalg.eig(A)

count = 0
for i in eigenvalues:
    count = count + 1
    print("Eigenwert {}: {:.5f}".format(count, i))
    print("Eigenvektor {}: {}".format(count, eigenvectors[count-1].round(5)))