import numpy as np
import matplotlib.pyplot as plt

# Definir el rango de valores de x evitando valores donde la función no está definida
x = np.linspace(-2, 1, 100)  # Evitamos valores mayores a 1
x = x[x <= 1]  # Nos aseguramos de que x <= 1

# Calcular Y = tan(sqrt(1 - x))
y = np.tan(np.sqrt(1 - x))

# Manejar los valores donde la tangente tiende a infinito (cerca de pi/2)
y[np.abs(y) > 10] = np.nan  # Evitamos grandes picos

# Graficar
plt.figure(figsize=(8, 6))
plt.plot(x, y, label=r'$Y = \tan(\sqrt{1 - x})$', color='b')

# Configuración del gráfico
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.xlabel("x")
plt.ylabel("Y")
plt.title("Gráfica de $Y = \\tan(\\sqrt{1 - x})$")
plt.legend()
plt.grid(True)

# Mostrar gráfico
plt.show()
