import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import sympy as sp


def secant_method_with_trace(function, x0, x1, tolerance, max_iterations):
    """ Sekantenverfahren mit Verfolgung jeder Iteration und benutzerdefinierten Einstellungen. """
    iterations_data = []
    for iteration in range(max_iterations):
        f_x0 = function(x0)
        f_x1 = function(x1)

        if abs(f_x1 - f_x0) < tolerance:
            raise ValueError("Division durch nahezu Null. Das Verfahren könnte scheitern.")

        # Berechnen des nächsten Wertes
        x2 = x1 - f_x1 * (x1 - x0) / (f_x1 - f_x0)
        iterations_data.append((iteration, x1, f_x1))

        if abs(x2 - x1) < tolerance:
            break

        x0, x1 = x1, x2

    return iterations_data


# Definieren der Funktion
x = sp.symbols('x')
f = x ** 2 - 2  # Funktion f(x) = x^2 - 2
f_lambdified = sp.lambdify(x, f)

# Benutzerdefinierte Einstellungen
x0 = 1  # Erster Startwert
x1 = 2  # Zweiter Startwert
custom_tolerance = 1e-6  # Toleranz
custom_max_iterations = 100  # Maximale Anzahl von Iterationen

# Ausführen des Sekantenverfahrens
trace_secant = secant_method_with_trace(
    f_lambdified, x0, x1, custom_tolerance, custom_max_iterations
)

# Erstellen einer DataFrame aus den Iterationsdaten des Sekantenverfahrens
results_table_secant = pd.DataFrame(trace_secant, columns=["Iteration", "x_n", "f(x_n)"])

# Erstellen des Plots
x_vals = np.linspace(0, 3, 400)
y_vals = f_lambdified(x_vals)

plt.figure(figsize=(10, 6))
plt.plot(x_vals, y_vals, label='f(x) = '+str(f))
plt.scatter(results_table_secant["x_n"], results_table_secant["f(x_n)"], color='red', label='Sekanten Iterations')
plt.title('Sekantenverfahren Iterationen und Ursprungsfunktion')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.axhline(0, color='black', linewidth=0.5)
plt.grid(True)
plt.legend()
plt.show()

# Ausgabe der Iterationsergebnisse
print(results_table_secant)
