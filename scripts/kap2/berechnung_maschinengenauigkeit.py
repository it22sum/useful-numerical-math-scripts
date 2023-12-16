def maschinengenauigkeit(B, n):
    # B = Basis, z.B. 10, 2, 16
    # n = Präzision / Mantisse
    eps = 1 / 2 * B ** (1 - n)
    return eps, f"{eps:.{n}f}"
