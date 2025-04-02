import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return (3**x - 3**-x) / (3**x + 3**-x)

x = np.linspace(-10, 10, 400)
y = f(x)

x_rounded = np.round(x, 4)
y_rounded = np.round(y, 4)

# Graficar la función
plt.plot(x, y)
plt.title(r'Gráfica de la función $\frac{3^x-3^{-x}}{3^x+3^{-x}}$')
plt.xlabel('x')
plt.ylabel('F(x)')
plt.axhline(0, color='black', linewidth=1)
plt.axvline(0, color='black', linewidth=1)
plt.grid(True)
plt.show()

# Calcular el índice medio
middle_index = len(x) // 2

# Crear una figura separada para la tabla de valores
plt.figure(figsize=(6, 4))

# Crear la tabla con los valores de x y f(x) redondeados
table_data = [
    ['x', 'f(x)'],
    [x_rounded[0], y_rounded[0]],  # Primer valor
    [x_rounded[middle_index], y_rounded[middle_index]],  # Valor medio
    [x_rounded[-1], y_rounded[-1]],  # Último valor
]

# Crear la tabla en la nueva figura
table = plt.table(cellText=table_data, loc='center', cellLoc='center', colWidths=[0.2, 0.2])

# Aumentar el tamaño de la fuente
table.auto_set_font_size(False)
table.set_fontsize(14)

# Escalar la tabla
table.scale(1.5, 1.5)

# Desactivar los ejes
plt.axis('off')

# Mostrar la tabla fuera de la gráfica
plt.show()
