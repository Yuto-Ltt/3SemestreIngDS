import numpy as np
import matplotlib.pyplot as plt

# Definir la función
def f(x):
    return (2*x + 3) / (4*x - 5)

# Crear rangos de valores para x
x1 = np.linspace(-10, 5/4 - 0.1, 400)  
x2 = np.linspace(5/4 + 0.1, 10, 400)   

# Calcular los valores de la función para ambos rangos
y1 = f(x1)
y2 = f(x2)

x1_rounded = np.round(x1, 4)
y1_rounded = np.round(y1, 4)

x2_rounded = np.round(x2, 4)
y2_rounded = np.round(y2, 4)

# Crear el gráfico
plt.figure(figsize=(8, 6))
plt.plot(x1, y1, color='b')
plt.plot(x2, y2, color='b')
plt.title(r'Gráfica de la funcion $\frac{2x + 3}{4x - 5}$')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.axhline(0, color='black', linewidth=1)
plt.axvline(0, color='black', linewidth=1)
plt.grid(True)
plt.show()

# Crear una figura separada para la tabla de valores
plt.figure(figsize=(6, 4))

# Crear la tabla con los valores de x y f(x) redondeados
table_data = [
    ['x', 'f(x)'],
    [x1_rounded[0], y1_rounded[0]],
    [x1_rounded[int(len(x1)/2)], y1_rounded[int(len(y1)/2)]],
    [x1_rounded[-1], y1_rounded[-1]],
    [x2_rounded[0], y2_rounded[0]],
    [x2_rounded[int(len(x2)/2)], y2_rounded[int(len(y2)/2)]],
    [x2_rounded[-1], y2_rounded[-1]],
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