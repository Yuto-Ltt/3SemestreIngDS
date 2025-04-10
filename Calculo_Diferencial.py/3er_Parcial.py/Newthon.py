import tkinter as tk
from tkinter import messagebox, ttk
from sympy import symbols, sympify, lambdify, diff


# --- Codificacion Pseudocodigo ---
def newton_raphson(f, f_deriv, r0, tolerancia=1e-6, max_iter=30):
    iteracion = 0
    error_absoluto = float('inf')
    pasos = []  # Lista para almacenar los pasos

    while error_absoluto > tolerancia and iteracion < max_iter:
        try:
            ra = r0 - f(r0) / f_deriv(r0)  # Raíz aproximada
        except ZeroDivisionError:
            print("Derivada igual a cero. No se puede continuar.")
            pasos.append((iteracion + 1, r0, "Error: derivada = 0", ""))
            return None, pasos

        error_absoluto = abs(ra - r0)
        pasos.append((iteracion + 1, r0, ra, error_absoluto))  # Guardar valores
        r0 = ra
        iteracion += 1

    if error_absoluto <= tolerancia:
        print(f"Raíz encontrada: {ra}")
        return ra, pasos
    else:
        print("El método no converge.")
        return None, pasos


# --- Interfaz f(x) ---
def ejecutar_metodo():
    for i in tabla.get_children():
        tabla.delete(i)  # Limpiar la tabla

    try:
        x = symbols('x')
        fx_expr = sympify(entry_fx.get())
        dfx_expr = diff(fx_expr, x)  # Derivada automática

        f = lambdify(x, fx_expr, modules=['numpy'])
        f_deriv = lambdify(x, dfx_expr, modules=['numpy'])

        r0 = float(entry_r0.get())
        tolerancia = float(entry_tol.get())
        max_iter = int(entry_max_iter.get())

        raiz, pasos = newton_raphson(f, f_deriv, r0, tolerancia, max_iter)

        # Mostrar los pasos en la tabla
        for paso in pasos:
            iter_num = paso[0]
            r0_val = f"{paso[1]:.6f}" if isinstance(paso[1], float) else paso[1]
            r1_val = f"{paso[2]:.6f}" if isinstance(paso[2], float) else paso[2]
            err = f"{paso[3]:.2e}" if isinstance(paso[3], float) else paso[3]
            tabla.insert("", "end", values=(iter_num, r0_val, r1_val, err))

        if raiz is not None:
            messagebox.showinfo("Resultado", f"Raíz aproximada: {raiz:.6f}\nDerivada usada: {dfx_expr}")
        else:
            messagebox.showwarning("Resultado", "El método no convergió.")

    except Exception as e:
        messagebox.showerror("Error", f"Ocurrió un error: {str(e)}")


# --- Crear ventana ---
ventana = tk.Tk()
ventana.title("Newton-Raphson")

tk.Label(ventana, text="f(x):").grid(row=0, column=0, sticky="e")
entry_fx = tk.Entry(ventana, width=40)
entry_fx.grid(row=0, column=1)

tk.Label(ventana, text="Valor inicial (r0):").grid(row=1, column=0, sticky="e")
entry_r0 = tk.Entry(ventana)
entry_r0.grid(row=1, column=1)

tk.Label(ventana, text="Tolerancia:").grid(row=2, column=0, sticky="e")
entry_tol = tk.Entry(ventana)
entry_tol.insert(0, "1e-6")
entry_tol.grid(row=2, column=1)

tk.Label(ventana, text="Máx. iteraciones:").grid(row=3, column=0, sticky="e")
entry_max_iter = tk.Entry(ventana)
entry_max_iter.insert(0, "30")
entry_max_iter.grid(row=3, column=1)

tk.Button(ventana, text="Ejecutar método", command=ejecutar_metodo).grid(row=4, column=0, columnspan=2, pady=10)

# --- Modificar la tabla para incluir columnas de r0 y r1 ---
tabla = ttk.Treeview(ventana, columns=("Iteración", "r0", "r1", "Error"), show="headings", height=10)
tabla.heading("Iteración", text="Iteración")
tabla.heading("r0", text="Valor Inicial (r0)")
tabla.heading("r1", text="Raíz Aproximada (r1)")
tabla.heading("Error", text="Error Absoluto")
tabla.grid(row=5, column=0, columnspan=2, padx=10, pady=10)

ventana.mainloop()
