import numpy as np
import matplotlib.pyplot as plt

# Definimos la función
def f(x):
    return 3 / x

# Derivada de la función
def df(x):
    return -3 / (x ** 2)  # Derivada de 3/x

# Punto donde queremos calcular la tangente
x1 = 3  # Valor de x en el punto de tangencia
y1 = f(x1)  # Valor de la función en x1
slope = df(x1)  # Pendiente de la tangente en x1

# Ecuación de la recta tangente: y - y1 = slope * (x - x1)
def tangent_line(x):
    return slope * (x - x1) + y1

# Rango de valores para la gráfica
x = np.linspace(0.5, 5, 100)
y = f(x)
tangent_y = tangent_line(x)

# Graficar
plt.figure(figsize=(10, 6))
plt.plot(x, y, label='Curva: f(x) = 3/x', color='blue')
plt.plot(x, tangent_y, label='Recta Tangente', color='red', linestyle='--')
plt.scatter([x1], [y1], color='green')  # Punto de la tangencia
plt.text(x1, y1, f'({x1}, {y1})', fontsize=12, verticalalignment='bottom')
plt.title('Curva y su Recta Tangente')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.axhline(0, color='black', linewidth=2)
plt.axvline(0, color='black', linewidth=2)
plt.grid()
plt.legend()
plt.show()
