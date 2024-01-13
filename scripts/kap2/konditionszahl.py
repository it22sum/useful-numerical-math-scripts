import numpy as np
import matplotlib.pyplot as plt

def f(x) : return x**(2) * np.sin(x)
def df(x): return 2*x*np.sin(x) + x**(2) * np.cos(x)
def K(x) : return np.abs(x)*np.abs(df(x))/np.abs(f(x))
# K = abs(x + 1)
x = np.arange(-4,2.05,0.05)
plt.plot(x,K(x),'-'), plt.xlabel('x'), plt.ylabel('K(x)')
plt.show()
# b)