import math

import sympy as sp

# Definieren Sie die Variable und die Funktion
x = sp.symbols('x')
funktion = sp.E**-x * x**2

# Berechnen Sie die Ableitung
ableitung = sp.diff(funktion, x)

print("Funktion:", funktion)
print("Ableitung:", ableitung)
