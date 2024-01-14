import math

import sympy as sp

def newton_iteration_formula(function):
    """Erstellt die Newton-Iterationsformel für eine gegebene Funktion."""
    # Definieren der symbolischen Variablen
    x = sp.symbols('x')

    # Berechnen der Ableitung
    derivative = sp.diff(function, x)

    # Newton-Iterationsformel
    newton_formula = x - function/derivative

    return sp.lambdify(x, newton_formula), newton_formula

# Definieren der symbolischen Variablen 'x'
x = sp.symbols('x')

# Beispiel: Newton-Iterationsformel für f(x) = x^2 - 2
f = sp.log(x)-1

newton_iteration_function, newton_iteration_symbolic = newton_iteration_formula(f)

# Zeigen der symbolischen Form der Newton-Iterationsformel
print(newton_iteration_symbolic)

