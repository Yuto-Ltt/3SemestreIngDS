import tkinter as tk
from tkinter import messagebox
from sympy import symbols, diff, lambdify

def newton_raphson(fx_str, x0, tol, max_iter):
    x = symbols('x')
    fx = eval(fx_str, {'x': x})  # Convertir string a expresión simbólica
    dfx = diff(fx, x)  # Derivada de f(x)
    
    f = lambdify(x, fx, 'math')  # Función evaluable
    df = lambdify(x, dfx, 'math')  # Derivada evaluable
    
    iter_count = 0
    while iter_count < max_iter:
        if df(x0) == 0:
            messagebox.showerror("Error", "Derivada cero, método no aplicable")
            return None
        
        x1 = x0 - f(x0) / df(x0)
        
        if abs(f(x1)) < tol:
            return x1
        
        x0 = x1
        iter_count += 1
    
    messagebox.showinfo("Resultado", f"El método no convergió después de {max_iter} iteraciones")
    return None

def calcular():
    try:
        fx_str = entrada_funcion.get()
        x0 = float(entrada_x0.get())
        tol = float(entrada_tol.get())
        max_iter = int(entrada_iter.get())
        
        raiz = newton_raphson(fx_str, x0, tol, max_iter)
        if raiz is not None:
            messagebox.showinfo("Resultado", f"Raíz encontrada: {raiz:.6f}")
    except Exception as e:
        messagebox.showerror("Error", f"Entrada inválida: {str(e)}")

# Configuración de la interfaz gráfica
root = tk.Tk()
root.title("Método de Newton-Raphson")

# Etiquetas y campos de entrada
tk.Label(root, text="Función f(x):").grid(row=0, column=0)
entrada_funcion = tk.Entry(root)
entrada_funcion.grid(row=0, column=1)

tk.Label(root, text="Valor inicial x0:").grid(row=1, column=0)
entrada_x0 = tk.Entry(root)
entrada_x0.grid(row=1, column=1)

tk.Label(root, text="Tolerancia ε:").grid(row=2, column=0)
entrada_tol = tk.Entry(root)
entrada_tol.grid(row=2, column=1)

tk.Label(root, text="Máx. Iteraciones:").grid(row=3, column=0)
entrada_iter = tk.Entry(root)
entrada_iter.grid(row=3, column=1)

# Botón de cálculo
boton_calcular = tk.Button(root, text="Calcular", command=calcular)
boton_calcular.grid(row=4, column=0, columnspan=2)

root.mainloop()