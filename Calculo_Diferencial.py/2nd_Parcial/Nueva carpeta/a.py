import sympy as sp
import numpy as np

# Inicializar la impresión simbólica para formato gráfico
sp.init_printing()

# Definir la variable simbólica
x = sp.Symbol('x')

# Definir la función f(x) = ∛x + √x
f = x**(1/3) + x**(1/2)

# Calcular la derivada simbólica
df_dx = sp.diff(f, x)

# Evaluar la derivada en x = 64
x_val = 64
df_dx_valor = df_dx.subs(x, x_val).evalf()

# Aproximación numérica con diferencias finitas
def f_num(x):
    return np.cbrt(x) + np.sqrt(x)

dx = 1e-6
df_dx_num = (f_num(x_val + dx) - f_num(x_val - dx)) / (2 * dx)  # Diferencias finitas

# Mostrar resultados
print("Función original: f(x) =", f)
print("Derivada simbólica: f'(x) =", df_dx)
print(f"Derivada simbólica evaluada en x={x_val}: {df_dx_valor}")
print(f"Derivada numérica en x={x_val} (Aprox. diferencias finitas): {df_dx_num}")
