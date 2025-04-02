import numpy as np
import matplotlib.pyplot as plt

#Definir la funcion
def f(x):
    return (np.abs(1 / (x + 1)) - 1 / 4) / (x - 3)


x1 = np.linspace(-10, -1.1, 200)  
x2 = np.linspace(-0.9, 2.9, 200) 
x3 = np.linspace(3.1, 10, 200)    
y1 = f(x1)
y2 = f(x2)
y3 = f(x3)

# Redondear los valores de x y f(x) a 4 decimales
x1_rounded = np.round(x1, 4)
y1_rounded = np.round(y1, 4)

x2_rounded = np.round(x2, 4)
y2_rounded = np.round(y2, 4)

x3_rounded = np.round(x3, 4)
y3_rounded = np.round(y3, 4)

plt.plot(x1, y1, color='b')
plt.plot(x2, y2, color='b')
plt.plot(x3, y3, color='b')
plt.title(r'Grafica de la funcion $\frac{|\frac{1}{x+1}| - \frac{1}{4}}{x-3}$')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.axhline(0, color='black', linewidth=1)
plt.axvline(0, color='black', linewidth=1)
plt.grid(True)
plt.legend()
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
    [x3_rounded[0], y3_rounded[0]],
    [x3_rounded[int(len(x3)/2)], y3_rounded[int(len(y3)/2)]],
    [x3_rounded[-1], y3_rounded[-1]]
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