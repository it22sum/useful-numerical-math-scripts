import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import sympy as sp

def simplified_newton_method_with_trace_customizable(function, derivative, start, tolerance, max_iterations):
    """ Vereinfachtes Newton-Verfahren mit Verfolgung jeder Iteration und benutzerdefinierten Einstellungen. """
    x_n = start
    f_prime_n = derivative(x_n)  # Berechnen der Ableitung nur einmal

    iterations_data = []
    for iteration in range(max_iterations):
        f_n = function(x_n)
        if abs(f_n) < tolerance:
            iterations_data.append((iteration, x_n, f_n))
            break

        iterations_data.append((iteration, x_n, f_n))

        # Update x_n mit der konstanten Ableitung
        x_n = x_n - f_n / f_prime_n

    return iterations_data

# Definieren der Funktion und ihrer Ableitung
x = sp.symbols('x')
f = 5*x**3+8*x**2 -1
f_prime = sp.diff(f, x)

f_lambdified = sp.lambdify(x, f)
f_prime_lambdified = sp.lambdify(x, f_prime)

# Benutzerdefinierte Einstellungen
start_value = 0.2  # Startwert
custom_tolerance = 1e-7  # Toleranz
custom_max_iterations = 100  # Maximale Anzahl von Iterationen

# Ausführen des vereinfachten Newton-Verfahrens
trace = simplified_newton_method_with_trace_customizable(
    f_lambdified, f_prime_lambdified, start_value, custom_tolerance, custom_max_iterations
)

# Erstellen einer DataFrame aus den Iterationsdaten
results_table = pd.DataFrame(trace, columns=["Iteration", "x_n", "f(x_n)"])

# Erstellen des Plots
x_vals = np.linspace(1, 2.5, 400)
y_vals = f_lambdified(x_vals)

plt.figure(figsize=(10, 6))
plt.plot(x_vals, y_vals, label='f(x) = '+str(f))
plt.scatter(results_table["x_n"], results_table["f(x_n)"], color='red', label='Newton Iterations')
plt.title('Newton-Verfahren vereinfacht Iterationen und Ursprungsfunktion')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.axhline(0, color='black', linewidth=0.5)
plt.grid(True)
plt.legend()
plt.show()

# Ausgabe der Iterationsergebnisse
print(results_table)

