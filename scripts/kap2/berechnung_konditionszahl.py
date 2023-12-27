import sympy as sp

def berechne_konditionszahl(funktion_str, x_0):
    # Definieren des symbolischen Variablen
    x = sp.symbols('x')

    # Umwandeln des Funktions-Strings in eine symbolische Funktion
    funktion = sp.sympify(funktion_str,locals={'e': sp.E})

    # Berechnen der Ableitung der Funktion
    funktion_prime = sp.diff(funktion, x)

    # Berechnen der Konditionszahl für den Punkt x_0
    if funktion.subs(x, x_0) != 0:
        konditionszahl = abs(x_0 * funktion_prime.subs(x, x_0) / funktion.subs(x, x_0))

    else:
        return "Fehler: Division durch Null"

    return konditionszahl


# Beispielanwendung
funktion_str = "1 - e**x"  # Funktion als String
x_0 = 1  # Punkt, an dem die Konditionszahl berechnet werden soll

konditionszahl = berechne_konditionszahl(funktion_str, x_0)
print("Konditionszahl der Funktion", funktion_str, "bei x =", x_0, ":", konditionszahl)
