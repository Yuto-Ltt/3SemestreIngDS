import tkinter as tk
from tkinter import messagebox
from sympy import symbols, sympify, lambdify


# --- Codificacion Pseudcodigo ---
def newton_raphson(f, f_deriv, r0, tolerancia=1e-6, max_iter=30):
    iteracion = 0
    error_absoluto = float('inf')

    while error_absoluto > tolerancia and iteracion < max_iter:
        try:
            ra = r0 - f(r0) / f_deriv(r0)
        except ZeroDivisionError:
            print("Derivada igual a cero. No se puede continuar.")
            return None

        error_absoluto = abs(ra - r0)
        r0 = ra
        iteracion += 1

    if error_absoluto <= tolerancia:
        print(f"Raíz encontrada: {ra}")
        return ra
    else:
        print("El método no converge.")
        return None


# --- Interfaz gráfica  ---
def ejecutar_metodo():
    try:
        x = symbols('x')
        fx_expr = sympify(entry_fx.get())
        dfx_expr = sympify(entry_dfx.get())

        f = lambdify(x, fx_expr, modules=['numpy'])
        f_deriv = lambdify(x, dfx_expr, modules=['numpy'])

        r0 = float(entry_r0.get())
        tolerancia = float(entry_tol.get())
        max_iter = int(entry_max_iter.get())

        raiz = newton_raphson(f, f_deriv, r0, tolerancia, max_iter)

        if raiz is not None:
            messagebox.showinfo("Resultado", f"Raíz aproximada: {raiz:.6f}")
        else:
            messagebox.showwarning("Resultado", "El método no convergió.")

    except Exception as e:
        messagebox.showerror("Error", f"Ocurrió un error: {str(e)}")


# --- Crear ventana ---
ventana = tk.Tk()
ventana.title("Newton-Raphson GUI")

tk.Label(ventana, text="f(x):").grid(row=0, column=0, sticky="e")
entry_fx = tk.Entry(ventana, width=30)
entry_fx.grid(row=0, column=1)

tk.Label(ventana, text="f'(x):").grid(row=1, column=0, sticky="e")
entry_dfx = tk.Entry(ventana, width=30)
entry_dfx.grid(row=1, column=1)

tk.Label(ventana, text="Valor inicial (r0):").grid(row=2, column=0, sticky="e")
entry_r0 = tk.Entry(ventana)
entry_r0.grid(row=2, column=1)

tk.Label(ventana, text="Tolerancia:").grid(row=3, column=0, sticky="e")
entry_tol = tk.Entry(ventana)
entry_tol.insert(0, "1e-6")
entry_tol.grid(row=3, column=1)

tk.Label(ventana, text="Máx. iteraciones:").grid(row=4, column=0, sticky="e")
entry_max_iter = tk.Entry(ventana)
entry_max_iter.insert(0, "30")
entry_max_iter.grid(row=4, column=1)

tk.Button(ventana, text="Ejecutar método", command=ejecutar_metodo).grid(row=5, column=0, columnspan=2, pady=10)

ventana.mainloop()
