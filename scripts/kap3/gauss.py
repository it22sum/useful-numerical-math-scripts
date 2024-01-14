import numpy as np


def gauss(A,b):
    A = A.astype('float64')
    b = b.astype('float64')
    det_factor = 1

    A_shape = np.shape(A)
    A_len = A_shape[0]


    print("--------------------------------")
    print("Spalten absteigend sortieren")
    print("--------------------------------")
    # Iterate all columns
    for y in range(A_len):

        # Iterate all rows
        for x in range(A_len):
            # All previous columns until current column have to be zero
            if (np.sum(np.absolute(A[x][:y])) != 0):
                continue

            # If the case, check if lower rows do not have zeroes
            for j in range(x + 1, A_len):
                if (np.sum(np.absolute(A[j][:y])) == 0):
                    continue

                # Swap rows
                A[[j, x]] = A[[x, j]]
                b[x], b[j] = b[j], b[x]
                print("Swap {} <-> {}".format(j, x))
                det_factor = det_factor * -1

    # Run Eliminations
    print("--------------------------------")
    print("Eliminationen")
    print("--------------------------------")
    # Iterate all Columns
    for y in range(A_len - 1):
        # Iterate all Rows
        for i in range(y, A_len):
            # Iterate rows below i
            for j in range(i+1, A_len):
                if (A[i][y] == 0):
                    continue
                # Calculate elimination factor for Column y
                # Makes A[j][y] become zero
                factor = (A[j][y])/(A[i][y])
                print("\nz{}=z{}-{}*z{}".format((j+1), (j+1), factor, (i+1)))

                # Apply factor to whole row
                A[j] = A[j] -factor*A[i]
                b[j] = b[j] -factor*b[i]
                print(A)
                print(b)

    # Calculate Result
    result = np.empty([A_len])

    print("\n--------")
    print("Rückwärtseinsetzen")
    print("--------")

    for x in range(A_len):
        # Start with last row (last x gets solved first)
        x_reverse = A_len - x - 1

        # Initial value: value of b
        x_result = b[x_reverse]
        print("\n\nb{}: {}".format(x_reverse+1, x_result))

        # Subtract all previously calculated x_n-factors
        for y in range(x_reverse + 1, A_len):
            print("Minus {}*b{}: {}*{}".format(A[x_reverse][y], y+1, A[x_reverse][y], result[y]))
            x_result = x_result - (A[x_reverse][y] * result[y])

        # Lastly, divide by the factor of the current x we're solving for
        x_result = x_result / A[x_reverse][x_reverse]
        print("Divide: {}".format(A[x_reverse][x_reverse]))
        print("b{}={}".format(x_reverse + 1, x_result))
        result[x_reverse] = x_result
    
    det = det_factor * np.prod(A.diagonal())
    return [A, det, result]

if __name__ == "__main__":
    A = np.array([
        [240, 120, 80],
        [60, 180, 170],
        [60, 90, 500],
    ])
    b = np.array([
        3080,
        4070,
        5030
        ])
    [A_triangle, detA, x] = gauss(A, b)
    print(x)
