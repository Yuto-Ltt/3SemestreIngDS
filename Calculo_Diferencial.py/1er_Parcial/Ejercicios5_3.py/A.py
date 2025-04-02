import numpy as np
import matplotlib.pyplot as plt

# Definir las funciones
def f1(x):
    return (-1/3 * x + 2)

def f2(x):
    return (-3 / x**2)

x1 = np.linspace(-10, 10, 3)
x2 = np.linspace(-10, 10, 6)
y1 = f1(x1)
y2 = f2(x2)

#Diseño de la grafica
plt.plot(x1, y1, label=r'$-\frac{1}{3}x + 2$', color='blue')
plt.plot(x2, y2, label=r'$-\frac{3}{x^2}$',)
plt.xlabel('x')
plt.ylabel('y')
plt.title('Gráficas de dos funciones')
plt.axhline(0, color='black', linewidth=1)
plt.axvline(0, color='black', linewidth=1)
plt.grid(True)
plt.show()
