import sympy as sp
def umwandeln_in_fixpunktform_korrigiert(func, x):
    """
    Wandelt eine Funktion in die Fixpunktform um, wenn sie nicht bereits in dieser Form ist.

    :param func: Die zu umwandelnde Funktion als Sympy-Ausdruck.
    :param x: Das symbolische Variable.
    :return: Die umgewandelte Funktion als String oder eine Nachricht, dass keine Umwandlung notwendig ist.
    """
    # Konvertieren der Funktion in einen Sympy-Ausdruck
    funktion_ausdruck = func(x)

    # Überprüfen, ob das 'x' in der Funktion positiv oder negativ vorkommt
    if funktion_ausdruck.has(x) and funktion_ausdruck.is_Add:
        koeffizient_von_x = funktion_ausdruck.as_coefficients_dict()[x]
        if koeffizient_von_x > 0:
            # Wenn x positiv ist, subtrahiere es
            fixpunktform = sp.Eq(x, funktion_ausdruck - x)
        else:
            # Wenn x negativ ist, addiere es
            fixpunktform = sp.Eq(x, funktion_ausdruck + x)
    else:
        # Funktion ist bereits in der Fixpunktform
        return "Die Funktion ist bereits in der Fixpunktform."

    return sp.pretty(fixpunktform)

# Sympy Symbol definieren
x = sp.symbols('x')

# Testfunktionen definieren
def f1(x): return (x - 0.3)**(1/3)
def f2(x): return x**2 - 2*x + 1
def f3(x): return x**3 - x + 0.3

# Umwandeln in Fixpunktform als Text und Testen
ergebnis_f1 = umwandeln_in_fixpunktform_korrigiert(f1, x)
ergebnis_f2 = umwandeln_in_fixpunktform_korrigiert(f2, x)
ergebnis_f3 = umwandeln_in_fixpunktform_korrigiert(f3, x)

print(ergebnis_f1)
print(ergebnis_f2)
print(ergebnis_f3)


