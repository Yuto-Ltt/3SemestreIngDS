import numpy as np
import matplotlib.pyplot as plt

# Definir la función
def f(x):
    return x / (x**2 + 5)

# Crear los valores para x e y
x = np.linspace(-10, 10, 400)
y = f(x)

# Graficar la función
plt.figure(figsize=(8, 6))
plt.plot(x, y)
plt.title(r'Gráfica de la función $\frac{x}{x^2 + 5}$')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.axhline(0, color='black', linewidth=1)
plt.axvline(0, color='black', linewidth=1)
plt.grid(True)

# Mostrar la gráfica
plt.show()

# Crear la tabla de valores en una imagen separada
x_values = np.linspace(-5, 5, 5)  # Algunos valores de x para la tabla
y_values = f(x_values)  # Evaluamos f(x) en esos valores

# Crear la figura para la tabla
fig, ax = plt.subplots(figsize=(5, 3))

# Ocultar los ejes de la tabla
ax.axis('off')

# Crear la tabla
column_labels = ['x', 'f(x)']
cell_text = [[f"{x:.2f}", f"{y:.2f}"] for x, y in zip(x_values, y_values)]

# Mostrar la tabla
ax.table(cellText=cell_text, colLabels=column_labels, loc='center', cellLoc='center', colColours=['#f5f5f5']*2)

# Mostrar la tabla
plt.show()

