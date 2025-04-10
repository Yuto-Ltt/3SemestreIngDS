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
            ra = r0 - f(r0) / f_deriv(r0)  # Raíz aproximada
        except ZeroDivisionError:
            print("Derivada igual a cero. No se puede continuar.")
            pasos.append((iteracion + 1, r0, "Error: derivada = 0", ""))
            return None, pasos

        error_absoluto = abs(ra - r0)
        pasos.append((iteracion + 1, r0, ra, error_absoluto))  # Guardar valores
        r0 = ra
        iteracion += 1

    if error_absoluto <= tolerancia:
        print(f"Raíz encontrada: {ra}")
        return ra, pasos
    else:
        print("El método no converge.")
        return None, pasos


# --- Interfaz f(x) ---
def ejecutar_metodo():
    for i in tabla.get_children():
        tabla.delete(i)  # Limpiar la tabla

    try:
        x = symbols('x')
        fx_expr = sympify(entry_fx.get())
        dfx_expr = diff(fx_expr, x)  # Derivada automática

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
            messagebox.showinfo("Resultado", f"Raíz aproximada: {raiz:.6f}\nDerivada usada: {dfx_expr}")
        else:
            messagebox.showwarning("Resultado", "El método no convergió.")

    except Exception as e:
        messagebox.showerror("Error", f"Ocurrió un error: {str(e)}")


# Configuración de la ventana principal
ventana = tk.Tk()
ventana.title("Método Newton-Raphson - Análisis Numérico")
ventana.geometry("1000x700")
ventana.configure(bg='#f5f5f5')
ventana.resizable(True, True)

# Estilo moderno
style = ttk.Style()
style.theme_use('clam')

# Configurar estilos
style.configure('TFrame', background='#f5f5f5')
style.configure('TLabel', background='#f5f5f5', font=('Roboto', 10))
style.configure('TButton', font=('Roboto', 10, 'bold'), padding=8, 
                background='#4CAF50', foreground='white')
style.map('TButton', background=[('active', '#45a049')])
style.configure('Title.TLabel', font=('Roboto', 14, 'bold'), 
               background='#3F51B5', foreground='white')
style.configure('Input.TFrame', background='#ffffff', 
               relief=tk.RAISED, borderwidth=1)
style.configure('Result.TLabel', font=('Roboto', 10, 'bold'),
               background='#f5f5f5', foreground='#3F51B5')

# Configurar estilo de la tabla
style.configure('Treeview', font=('Roboto', 9), rowheight=25)
style.configure('Treeview.Heading', font=('Roboto', 10, 'bold'), 
               background='#3F51B5', foreground='white')
style.map('Treeview', background=[('selected', '#BBDEFB')])
style.configure('Treeview', fieldbackground='#ffffff')

# Crear tags para filas alternadas
tabla_tag_style = ttk.Style()
tabla_tag_style.configure('evenrow.Treeview', background='#f5f5f5')
tabla_tag_style.configure('oddrow.Treeview', background='#e9e9e9')

# Marco principal con degradado (simulado)
header_frame = ttk.Frame(ventana, style='Title.TLabel', height=80)
header_frame.pack(fill=tk.X)
ttk.Label(header_frame, text="MÉTODO NEWTON-RAPHSON", 
         style='Title.TLabel').pack(pady=20)

# Marco de contenido principal
main_frame = ttk.Frame(ventana, padding="20 15")
main_frame.pack(fill=tk.BOTH, expand=True)

# Panel de entrada de datos (tarjeta)
input_card = ttk.Frame(main_frame, style='Input.TFrame', padding=15)
input_card.pack(fill=tk.X, pady=(0, 15))

# Configuración de grid para inputs
input_card.columnconfigure(1, weight=1)

# Campos de entrada con etiquetas modernas
ttk.Label(input_card, text="Función f(x):", 
         font=('Roboto', 10, 'bold')).grid(row=0, column=0, padx=5, pady=5, sticky="e")
entry_fx = ttk.Entry(input_card, width=45, font=('Roboto', 10))
entry_fx.grid(row=0, column=1, padx=5, pady=5, sticky="we")
entry_fx.insert(0, "x*3 - 2*x*2 - 5*x + 6")

ttk.Label(input_card, text="Valor inicial (r₀):", 
         font=('Roboto', 10, 'bold')).grid(row=1, column=0, padx=5, pady=5, sticky="e")
entry_r0 = ttk.Entry(input_card, font=('Roboto', 10))
entry_r0.grid(row=1, column=1, padx=5, pady=5, sticky="we")
entry_r0.insert(0, "-3")

ttk.Label(input_card, text="Tolerancia:", 
         font=('Roboto', 10, 'bold')).grid(row=2, column=0, padx=5, pady=5, sticky="e")
entry_tol = ttk.Entry(input_card, font=('Roboto', 10))
entry_tol.grid(row=2, column=1, padx=5, pady=5, sticky="we")
entry_tol.insert(0, "1e-6")

ttk.Label(input_card, text="Máx. iteraciones:", 
         font=('Roboto', 10, 'bold')).grid(row=3, column=0, padx=5, pady=5, sticky="e")
entry_max_iter = ttk.Entry(input_card, font=('Roboto', 10))
entry_max_iter.grid(row=3, column=1, padx=5, pady=5, sticky="we")
entry_max_iter.insert(0, "30")

# Botones de acción
button_frame = ttk.Frame(main_frame)
button_frame.pack(fill=tk.X, pady=(10, 15))

ttk.Button(button_frame, text="Ejecutar Método", command=ejecutar_metodo, 
          style='TButton').pack(side=tk.LEFT, padx=5)
grafico_btn = ttk.Button(button_frame, text="Ver Gráfico", state=tk.DISABLED,
                        style='TButton')
grafico_btn.pack(side=tk.LEFT, padx=5)
ttk.Button(button_frame, text="Limpiar", command=lambda: [
          entry.delete(0, tk.END) for entry in [entry_fx, entry_r0, entry_tol, entry_max_iter]],
          style='TButton').pack(side=tk.RIGHT, padx=5)

# Tabla de resultados con scrollbar
table_frame = ttk.Frame(main_frame)
table_frame.pack(fill=tk.BOTH, expand=True)

# Añadir scrollbars
scroll_y = ttk.Scrollbar(table_frame)
scroll_x = ttk.Scrollbar(table_frame, orient=tk.HORIZONTAL)

tabla = ttk.Treeview(table_frame, 
                    columns=("Iteración", "r₀", "r₁", "Error"), 
                    show="headings",
                    yscrollcommand=scroll_y.set,
                    xscrollcommand=scroll_x.set,
                    height=12)

scroll_y.config(command=tabla.yview)
scroll_x.config(command=tabla.xview)

# Configurar columnas
tabla.heading("Iteración", text="Iteración", anchor=tk.CENTER)
tabla.heading("r₀", text="Valor Inicial (r₀)", anchor=tk.CENTER)
tabla.heading("r₁", text="Raíz Aproximada (r₁)", anchor=tk.CENTER)
tabla.heading("Error", text="Error Absoluto", anchor=tk.CENTER)

tabla.column("Iteración", width=80, anchor=tk.CENTER)
tabla.column("r₀", width=200, anchor=tk.CENTER)
tabla.column("r₁", width=200, anchor=tk.CENTER)
tabla.column("Error", width=150, anchor=tk.CENTER)

# Empaquetar tabla y scrollbars
scroll_y.pack(side=tk.RIGHT, fill=tk.Y)
scroll_x.pack(side=tk.BOTTOM, fill=tk.X)
tabla.pack(fill=tk.BOTH, expand=True)

# Panel de resultados (tarjeta)
result_card = ttk.Frame(main_frame, style='Input.TFrame', padding=15)
result_card.pack(fill=tk.X, pady=(15, 0))

resultado_var = tk.StringVar(value="Esperando cálculo...")
derivada_var = tk.StringVar()

ttk.Label(result_card, text="RESULTADOS", 
         font=('Roboto', 11, 'bold'), 
         foreground='#3F51B5').pack(anchor=tk.W)

result_frame = ttk.Frame(result_card)
result_frame.pack(fill=tk.X, pady=5)

ttk.Label(result_frame, text="Raíz:", 
         font=('Roboto', 10, 'bold')).grid(row=0, column=0, sticky="e")
ttk.Label(result_frame, textvariable=resultado_var, 
         font=('Roboto', 10)).grid(row=0, column=1, sticky="w", padx=10)

ttk.Label(result_frame, text="Derivada:", 
         font=('Roboto', 10, 'bold')).grid(row=1, column=0, sticky="e")
ttk.Label(result_frame, textvariable=derivada_var, 
         font=('Roboto', 10), wraplength=600).grid(row=1, column=1, sticky="w", padx=10)

# Mejorar el redimensionamiento
ventana.columnconfigure(0, weight=1)
ventana.rowconfigure(0, weight=1)

ventana.mainloop()