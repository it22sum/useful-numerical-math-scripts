import numpy as np
from fractions import Fraction

fractionize = np.vectorize(lambda x: Fraction(x).limit_denominator())

eye = np.eye(3)

print("=========================================================\n"
      "Die folgenden Ergebnisse und Berechnungen sind Beispiele.\n"
      "=========================================================\n")

print("Matrix mit Gleitkommazahlen:")
print(eye - 2 * 1/np.sqrt(38) * 1/np.sqrt(38) * np.array([3, -5, 2]) * np.array([3, -5, 2]).transpose())


print("\nDieselbe Matrix aber mit Brüchen:")
print("\tFYI: Fraction(-93, 76): -93/76.")
print(fractionize(eye - 2 * 1/np.sqrt(38) * 1/np.sqrt(38) * np.array([6.5, -5, 2]) * np.array([6.5, -5, 2]).transpose()))