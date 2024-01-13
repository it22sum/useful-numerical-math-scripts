import numpy as np

def calculate_machine_epsilon():
    epsilon = B / 2 * B ** (-n)
    return epsilon

B = 2  # Basis für binäre Systeme
n = 46

epsilon = calculate_machine_epsilon()
print("Maschinengenauigkeit: ", epsilon)
