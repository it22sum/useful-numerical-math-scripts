def jacobi_gauss_seidel(A, b, x0, tol, opt):
    # opt := boolean - isJacobi
    import numpy as np

    if A.shape[0] != A.shape[1]:
        raise ValueError('Matrix A muss NxN sein.')

    def iteration(B, C, current_x):

        next_x = B @ current_x + C
        # print("Iteration, nächstes x:", next_x)
        return next_x

    def a_priori(B, x0, x1, tol):
        bnorm = np.linalg.norm(B, np.inf)

        calculatedSteps = np.log(tol / np.linalg.norm(x1 - x0, np.inf) * (1 - bnorm)) / np.log(bnorm)
        calculatedSteps += 1  # +1 da wir sozusagen bereits einen Schritt gemacht haben.

        return calculatedSteps

    def calucate_B_C(A, b, opt):
        # B and C werden in jeweils in Jacobi sowie in Gauss-Seidel benötigt.
        D = np.diag(np.diag(A))
        L = np.tril(A, k=-1)
        R = np.triu(A, k=1)

        if opt:
            # Jacobi
            B = (-np.linalg.inv(D)) @ (L + R)
            C = np.linalg.inv(D) @ b
        else:
            # Gauss-Seidel
            B = (-np.linalg.inv(D + L)) @ R
            C = np.linalg.inv(D + L) @ b

        # 'Löschen von D, L, R um nicht mehr benötigten Speicher freizugeben.
        D = 0
        L = 0
        R = 0

        return B, C

    B, C = calucate_B_C(A, b, opt)

    xn = iteration(B, C, x0)
    xprev = x0
    n = 0
    n2 = a_priori(B, x0, xn, tol)
    while np.linalg.norm(xn - xprev, np.inf) > tol:
        xprev = xn
        xn = iteration(B, C, xn)
        n += 1

    return xn, n, n2


if __name__ == "__main__":
    import numpy as np
    A = np.array([
        [8, 5, 2],
        [5, 9, 1],
        [4, 2, 7]
    ])

    b = np.array([19, 5, 34])
    #x0 = np.array([1, -1, 3])
    x0 = np.array([2.0511, -1.0134, 3.9746])

    print(jacobi_gauss_seidel(A, b, x0, 1e-4, False))
