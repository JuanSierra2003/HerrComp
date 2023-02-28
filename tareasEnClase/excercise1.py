import scipy as sp
import random
import numpy as np
from matplotlib import pyplot as plt

def function(X, coe):
	return coe[0] + coe[1]*X + coe[2]*X**2 + coe[3]*X**3 

X = np.linspace(-5, 5, 200)
Y = function(X, (1, 0.3, 0.5, 0.1)) + np.random.normal(0, 1, 200)

def theoretical(x,a,b,c,d):
  return a + b*x + c*x**2 + d*x**3

popt , pcov = sp.optimize.curve_fit(theoretical, X,Y)

Yr = function(X, popt)

plt.scatter(X, Y, color="blue", label="Noisy data")
plt.plot(X, Yr, color="red", label="Fit", linewidth=3)

plt.xlabel("X")
plt.ylabel("Y")
plt.legend()
plt.show()

print(popt)
print(pcov)

"""
Juan Sebastian Sierra Jaraba
Federico Villadiego Forero
Daniel Felipe Rojas Paternina
Daniel Alejandro Pineda
Giovanni Aldana Guzman
Yojhan Andres Angel Arias
"""