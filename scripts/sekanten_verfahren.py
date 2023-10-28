def sekanten_verfahren(f, x0, x1, tolerance):

    if f(x0) < 0 < f(x1) or f(x0) > 0 > f(x1):
        print("Die Funktion f(x) mit [{a}, {b}] besitzt definitiv eine Nullstelle.".format(a=x0, b=x1))

    x_n_minus_1 = x0
    x_n = x1

    # WENN f(x_n - tolerance) * f(x_n + tolerance) < 0
    #       DANN => | x_n - x̄ | < tolerance
    #            => Wert ist genug genau, um als "richtige" Lösung
    #               akzeptiert zu werden.

    while f(x_n - tolerance) * f(x_n + tolerance) >= 0:  # abs(f(x_n)) >= tolerance:
        x2 = x_n - ((x_n - x_n_minus_1) / (f(x_n) - f(x_n_minus_1))) * f(x_n)
        x_n_minus_1 = x_n
        x_n = x2


    return x_n


# Hier Funktion definieren:
def funktion(x):
    return x ** 3 + 3 * x ** 2 + 12 * x + 8


print("Nullstelle: " + str(sekanten_verfahren(funktion, -5, 5, 0.01)))
