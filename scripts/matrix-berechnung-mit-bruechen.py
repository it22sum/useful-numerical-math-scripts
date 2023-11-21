import numpy as np
from fractions import Fraction

fractionize = np.vectorize(lambda x: Fraction(x).limit_denominator())

eye = np.eye(3)

print("=========================================================\n"
      "Die folgenden Ergebnisse und Berechnungen sind Beispiele.\n"
      "=========================================================\n")

func = eye - 2 * 1/np.sqrt(38) * 1/np.sqrt(38) * np.array([3, -5, 2]) * np.array([3, -5, 2]).transpose()

print("Matrix mit Gleitkommazahlen:")
print(func)

print("\nDieselbe Matrix aber mit Brüchen:")
print("\tFYI: Fraction(10, 19): 10/19.")
print(fractionize(func))