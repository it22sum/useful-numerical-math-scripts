import numpy as np

def rel(A,b,tol_A,tol_b):
    A_f = A+tol_A
    b_f= b+tol_b
    A_inv = np.linalg.inv(A)
    cond = np.linalg.norm(A, np.inf) * np.linalg.norm(A_inv, np.inf)
    A_rel = np.linalg.norm(A - A_f, np.inf) / np.linalg.norm(A, np.inf)
    b_rel = np.linalg.norm(b-b_f, np.inf) / np.linalg.norm(b, np.inf)

    if cond * A_rel > 1:
        return print("Bedingung nicht erfüllt con * A_rel < 1")

    part1 = cond / (1 - cond * A_rel)
    part2 = A_rel + b_rel

    print("Fehlerbehaftete Matirx A: \n" + str(A_f))
    print("Fehlerbehafteter Vektor b: \n" + str(b_f))
    print("Kondition der Matrix A:" + str(cond))
    print("Relativer Fehler der Matrix A:" + str(A_rel))
    print("Relativer Fehler des Vektors b:" + str(b_rel))
    print("Part1:" + str(part1))
    print("Part2:" + str(part2))
    print("Lösung(Part1 * Part2):" + str(part1 * part2))

A=np.array([[20000,30000,10000],[10000,17000,6000],[2000,3000,2000]])
b = np.array([[5.72e6],[3.3e6],[0.836e6]])
tol_A = 100
tol_b = 0.1e6

rel(A,b,tol_A,tol_b)

def abs_f(A,b,tol_b):
    A_inv = np.linalg.inv(A)
    b_f = b + tol_b
    b_rel= np.linalg.norm(b-b_f,np.inf)
    norm_A_inv = np.linalg.norm(A_inv,np.inf)
    result = norm_A_inv*b_rel

    print("Inverse Matrix A_inv: \n" + str(A_inv))
    print("Fehlerbehafteter Vektor b: \n" + str(b_f))
    print("Norm der Inversen Matrix A_inv:" + str(norm_A_inv))
    print("Relativer Fehler des Vektors b:" + str(b_rel))
    print("Lösung:" + str(result))

abs_f(A,b,tol_b)

