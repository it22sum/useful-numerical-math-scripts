import math

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import sympy as sp

def newton_method_with_trace(function, derivative, start, tolerance, max_iterations):
    """ Newton-Verfahren mit Verfolgung jeder Iteration und benutzerdefinierten Einstellungen. """
    x_n = start

    iterations_data = []
    for iteration in range(max_iterations):
        f_n = function(x_n)
        f_prime_n = derivative(x_n)  # Berechnen der Ableitung in jedem Schritt

        if abs(f_n) < tolerance:
            iterations_data.append((iteration, x_n, f_n))
            break

        if abs(f_prime_n) < tolerance:
            raise ValueError("Die Ableitung ist nahe Null. Das Verfahren könnte scheitern.")

        iterations_data.append((iteration, x_n, f_n))

        # Update x_n basierend auf der aktuellen Ableitung
        x_n = x_n - f_n / f_prime_n

    return iterations_data

# Definieren der Funktion und ihrer Ableitung
x = sp.symbols('x')
f = 5*x**3+8*x**2 -1
f_prime = sp.diff(f, x)

f_lambdified = sp.lambdify(x, f)
f_prime_lambdified = sp.lambdify(x, f_prime)

# Benutzerdefinierte Einstellungen
start_value = 0.5  # Startwert
custom_tolerance = 1e-10  # Toleranz
custom_max_iterations = 500  # Maximale Anzahl von Iterationen

# Ausführen des Newton-Verfahrens
trace_newton = newton_method_with_trace(
    f_lambdified, f_prime_lambdified, start_value, custom_tolerance, custom_max_iterations
)

# Erstellen einer DataFrame aus den Iterationsdaten des Newton-Verfahrens
results_table_newton = pd.DataFrame(trace_newton, columns=["Iteration", "x_n", "f(x_n)"])

# Erstellen des Plots
x_vals = np.linspace(1, 2.5, 400)
y_vals = f_lambdified(x_vals)

plt.figure(figsize=(10, 6))
plt.plot(x_vals, y_vals, label='f(x) =' + str(f))
plt.scatter(results_table_newton["x_n"], results_table_newton["f(x_n)"], color='red', label='Newton Iterations')
plt.title('Newton-Verfahren Iterationen und Ursprungsfunktion')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.axhline(0, color='black', linewidth=0.5)
plt.grid(True)
plt.legend()
plt.show()

# Ausgabe der Iterationsergebnisse
print(results_table_newton)
