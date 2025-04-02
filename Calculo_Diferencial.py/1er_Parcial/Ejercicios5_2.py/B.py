import numpy as np
import matplotlib.pyplot as plt

def f(x):
    denominator = 6 + x - 3*x**2
    with np.errstate(divide='ignore', invalid='ignore'):
        return (2*x**2 + 1) / denominator

a = -3
b = 1
c = 6
discriminante = b**2 - 4*a*c
raiz1 = (-b + np.sqrt(discriminante)) / (2*a)
raiz2 = (-b - np.sqrt(discriminante)) / (2*a)

print(f"Puntos donde el denominador se hace cero: x = {raiz1}, x = {raiz2}")

x1 = np.linspace(-10, raiz1 - 0.1, 400)
x2 = np.linspace(raiz2 + 0.1, 10, 400)

x_positive = np.linspace(raiz1 + 0.01, raiz2 - 0.01, 400)

y1 = f(x1)
y2 = f(x2)
y_positive = f(x_positive)

# Crear la gráfica
plt.figure(figsize=(8, 6))

plt.plot(x1, y1, color='b', linewidth=2)
plt.plot(x2, y2, color='b', linewidth=2)
plt.plot(x_positive, y_positive, color='b', linewidth=2)

plt.title('Gráfica de la función $f(x) = \\frac{2x^2 + 1}{6 + x - 3x^2}$')
plt.axhline(0, color='black', linewidth=1)
plt.axvline(0, color='black', linewidth=1)
plt.xlabel('x')
plt.ylabel('f(x)')
plt.legend()
plt.grid(True)

# Mostrar la gráfica
plt.show()

# Ahora crear la tabla de valores en una imagen separada
x_values = np.linspace(-2, 2, 5)  # Valores de x para la tabla
y_values = f(x_values)  # Evaluamos f(x) en esos valores

# Crear la figura para la tabla
fig, ax = plt.subplots(figsize=(5, 3))

# Ocultar los ejes ya que solo necesitamos la tabla
ax.axis('off')

# Crear la tabla
column_labels = ['x', 'f(x)']
cell_text = [[f"{x:.2f}", f"{y:.2f}"] for x, y in zip(x_values, y_values)]

# Mostrar la tabla
ax.table(cellText=cell_text, colLabels=column_labels, loc='center', cellLoc='center', colColours=['#f5f5f5']*2)

# Mostrar la tabla
plt.show()
