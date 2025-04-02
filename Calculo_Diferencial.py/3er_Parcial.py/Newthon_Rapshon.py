import sympy as sp
import tkinter as tk
from tkinter import messagebox

def newton_raphson(f_expr, x0, tol=1e-6, max_iter=100):
    x = sp.symbols('x')
    f = sp.sympify(f_expr)  # Convierte la expresión en una función simbólica
    f_prime = sp.diff(f, x)  # Derivada de la función
    
    f_lambda = sp.lambdify(x, f)  # Convierte la función en una expresión evaluable
    f_prime_lambda = sp.lambdify(x, f_prime)
    
    x_n = x0  # Valor inicial
    
    for i in range(max_iter):
        fx_n = f_lambda(x_n)
        fpx_n = f_prime_lambda(x_n)
        
        if abs(fpx_n) < 1e-10:  # Evita la división por cero
            raise ValueError("La derivada es demasiado pequeña, posible punto crítico.")
        
        x_next = x_n - fx_n / fpx_n
        
        if abs(x_next - x_n) < tol:
            return x_next  # Se encontró la raíz con la tolerancia deseada
        
        x_n = x_next
    
    raise ValueError("No se encontró la raíz en el número máximo de iteraciones.")

def calcular_raiz():
    try:
        funcion = entry_funcion.get()
        x0 = float(entry_x0.get())
        tol = float(entry_tol.get())
        max_iter = int(entry_max_iter.get())
        
        raiz = newton_raphson(funcion, x0, tol, max_iter)
        messagebox.showinfo("Resultado", f"Raíz encontrada: {raiz}")
    except ValueError as e:
        messagebox.showerror("Error", str(e))
    except Exception:
        messagebox.showerror("Error", "Entrada no válida. Verifique los valores ingresados.")

# Crear ventana principal
root = tk.Tk()
root.title("Calculadora Newton-Raphson")
root.geometry("400x300")  # Aumenta el tamaño de la ventana

tk.Label(root, text="Función f(x):", font=("Arial", 12)).grid(row=0, column=0, padx=10, pady=10)
entry_funcion = tk.Entry(root, width=30)
entry_funcion.grid(row=0, column=1, padx=10, pady=10)

tk.Label(root, text="Valor inicial x0:", font=("Arial", 12)).grid(row=1, column=0, padx=10, pady=10)
entry_x0 = tk.Entry(root, width=30)
entry_x0.grid(row=1, column=1, padx=10, pady=10)

tk.Label(root, text="Tolerancia:", font=("Arial", 12)).grid(row=2, column=0, padx=10, pady=10)
entry_tol = tk.Entry(root, width=30)
entry_tol.grid(row=2, column=1, padx=10, pady=10)

tk.Label(root, text="Máx. iteraciones:", font=("Arial", 12)).grid(row=3, column=0, padx=10, pady=10)
entry_max_iter = tk.Entry(root, width=30)
entry_max_iter.grid(row=3, column=1, padx=10, pady=10)

tk.Button(root, text="Calcular", font=("Arial", 12), command=calcular_raiz, width=15).grid(row=4, columnspan=2, pady=20)

root.mainloop()
