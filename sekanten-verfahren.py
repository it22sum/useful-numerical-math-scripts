import numpy as np


def sekanten_verfahren(f, x0, x1, tolerance):
    x_n_minus_1 = x0
    x_n = x1

    # WENN f(x_n - tolerance) * f(x_n + tolerance) < 0
    #       DANN => | x_n - x̄ | < tolerance
    #            => Wert ist genug genau, um als "richtige" Lösung
    #               akzeptiert zu werden.

    while f(x_n - tolerance) * f(x_n + tolerance) >= 0:
        x2 = x0 - ((x_n - x_n_minus_1) / (f(x_n) - f(x_n - 1))) * f(x_n)
        x_n_minus_1 = x_n
        x_n = x2

    return x_n

# Hier Funktion definieren:
def f(x) :
    return x ** 2


