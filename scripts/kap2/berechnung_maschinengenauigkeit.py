def maschinengenauigkeit(B, n):
    # B = Basis, z.B. 10, 2, 16
    # n = Präzision / Mantisse
    eps = B / 2 * B ** (-n)
    return eps, f"{eps:.{n}f}"


if __name__ == '__main__':
    B = 2  # Basis für binäre Systeme
    n = 46

    epsilon = maschinengenauigkeit(B,n)
    print("Maschinengenauigkeit: ", epsilon)