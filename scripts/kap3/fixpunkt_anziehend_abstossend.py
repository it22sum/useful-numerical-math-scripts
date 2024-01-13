def check_fixed_point(func, point):
    import sympy as sp

    # Ableitung der Funktion berechnen
    derivative = sp.diff(func, x)

    # Wert der Ableitung am Fixpunkt berechnen
    derivative_at_point = derivative.subs(x, point).evalf()

    # Überprüfen, ob der Fixpunkt anziehend oder abstoßend ist
    if abs(derivative_at_point) < 1:
        return "anziehend"
    elif abs(derivative_at_point) > 1:
        return "abstoßend"
    else:
        return "neutral oder nicht bestimmbar"


if __name__ == '__main__':
    import sympy as sp

    # Symbol definieren
    x = sp.symbols('x')

    # Funktion definieren (Beispiel)
    f = x ** 3 + 0.3

    # Fixpunkte definieren
    fixed_points = [-1.125, 0.3389, 0.7864]

    # Ergebnisse für jeden Fixpunkt ausgeben
    results = {fp: check_fixed_point(f, fp) for fp in fixed_points}
    print("f = " + str(f))
    print(results)
