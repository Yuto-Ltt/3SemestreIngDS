import numpy as np
import matplotlib.pyplot as plt

#Definir funcion
def f(x):
    return (-2*x)

#Valores para x
x = np.linspace(-10, 10, 400)
y = f(x)

#Definir grafico
plt.plot(x,y)
plt.title(r'Grafico de la funcion ${-2x}$')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.axhline(0, color = 'black', linewidth = 1)
plt.axvline(0, color = 'black', linewidth = 1)
plt.grid(True)
plt.show()
