# Importamos las librerías necesarias
import tkinter as tk  # Para crear la interfaz gráfica
from tkinter import messagebox, ttk  # Para manejar cuadros de mensaje y tablas
from sympy import symbols, sympify, lambdify, diff  # Para trabajar con expresiones matemáticas

# --- Codificación del pseudocódigo del método de Newton-Raphson ---
def newton_raphson(f, f_deriv, r0, tolerancia=1e-6, max_iter=30):
    # Inicializamos variables para el número de iteraciones y el error
    iteracion = 0
    error_absoluto = float('inf')  # Inicializamos el error en infinito
    pasos = []  # Lista para almacenar los pasos del proceso

    # Comenzamos el ciclo mientras el error sea mayor que la tolerancia y no se haya alcanzado el máximo de iteraciones
    while error_absoluto > tolerancia and iteracion < max_iter:
        try:
            # Aplicamos la fórmula de Newton-Raphson para encontrar una nueva raíz aproximada
            ra = r0 - f(r0) / f_deriv(r0)
        except ZeroDivisionError:
            # Si la derivada es cero, no se puede continuar
            print("Derivada igual a cero. No se puede continuar.")
            pasos.append((iteracion + 1, r0, "Error: derivada = 0", ""))
            return None, pasos

        # Calculamos el error absoluto entre la nueva raíz y la anterior
        error_absoluto = abs(ra - r0)
        # Guardamos los resultados del paso actual (iteración, valor inicial, nueva raíz, error)
        pasos.append((iteracion + 1, r0, ra, error_absoluto))
        r0 = ra  # Actualizamos el valor de r0 para la siguiente iteración
        iteracion += 1  # Incrementamos el número de iteración

    # Verificamos si el error es menor o igual a la tolerancia
    if error_absoluto <= tolerancia:
        print(f"Raíz encontrada: {ra}")
        return ra, pasos  # Retornamos la raíz encontrada y los pasos
    else:
        print("El método no converge.")
        return None, pasos  # Si no converge, retornamos None

# --- Función para ejecutar el método con la interfaz gráfica ---
def ejecutar_metodo():
    # Limpiar la tabla de resultados antes de mostrar los nuevos resultados
    for i in tabla.get_children():
        tabla.delete(i)

    try:
        # Definimos la variable simbólica 'x' para la función matemática
        x = symbols('x')
        # Obtenemos la expresión de la función a partir de la entrada de texto
        fx_expr = sympify(entry_fx.get())
        # Calculamos la derivada de la función con respecto a 'x'
        dfx_expr = diff(fx_expr, x)

        # Creamos funciones lambda para evaluar la función y su derivada
        f = lambdify(x, fx_expr, modules=['numpy'])
        f_deriv = lambdify(x, dfx_expr, modules=['numpy'])

        # Obtenemos los valores de r0, tolerancia y número máximo de iteraciones desde la interfaz gráfica
        r0 = float(entry_r0.get())
        tolerancia = float(entry_tol.get())
        max_iter = int(entry_max_iter.get())

        # Llamamos al método de Newton-Raphson para obtener la raíz y los pasos
        raiz, pasos = newton_raphson(f, f_deriv, r0, tolerancia, max_iter)

        # Mostramos los pasos en la tabla
        for paso in pasos:
            iter_num = paso[0]
            # Formateamos los valores de r0, r1 y el error para que tengan un número fijo de decimales
            r0_val = f"{paso[1]:.6f}" if isinstance(paso[1], float) else paso[1]
            r1_val = f"{paso[2]:.6f}" if isinstance(paso[2], float) else paso[2]
            err = f"{paso[3]:.2e}" if isinstance(paso[3], float) else paso[3]
            # Insertamos los datos de la iteración en la tabla
            tabla.insert("", "end", values=(iter_num, r0_val, r1_val, err))

        # Si se encontró una raíz, mostramos un mensaje con el resultado
        if raiz is not None:
            messagebox.showinfo("Resultado", f"Raíz aproximada: {raiz:.6f}\nDerivada usada: {dfx_expr}")
        else:
            messagebox.showwarning("Resultado", "El método no convergió.")

    except Exception as e:
        # Si ocurre un error durante la ejecución, mostramos un mensaje de error
        messagebox.showerror("Error", f"Ocurrió un error: {str(e)}")


# --- Crear la ventana principal de la interfaz gráfica ---
ventana = tk.Tk()  # Creamos la ventana principal
ventana.title("Newton-Raphson")  # Establecemos el título de la ventana

# Creamos los elementos de la interfaz para ingresar la función y los parámetros
tk.Label(ventana, text="f(x):").grid(row=0, column=0, sticky="e")
entry_fx = tk.Entry(ventana, width=40)  # Campo de texto para la función
entry_fx.grid(row=0, column=1)

tk.Label(ventana, text="Valor inicial (r0):").grid(row=1, column=0, sticky="e")
entry_r0 = tk.Entry(ventana)  # Campo de texto para el valor inicial (r0)
entry_r0.grid(row=1, column=1)

tk.Label(ventana, text="Tolerancia:").grid(row=2, column=0, sticky="e")
entry_tol = tk.Entry(ventana)  # Campo de texto para la tolerancia
entry_tol.insert(0, "1e-6")  # Valor predeterminado de tolerancia
entry_tol.grid(row=2, column=1)

tk.Label(ventana, text="Máx. iteraciones:").grid(row=3, column=0, sticky="e")
entry_max_iter = tk.Entry(ventana)  # Campo de texto para el número máximo de iteraciones
entry_max_iter.insert(0, "30")  # Valor predeterminado de iteraciones
entry_max_iter.grid(row=3, column=1)

# Creamos un botón que ejecuta el método de Newton-Raphson cuando se hace clic
tk.Button(ventana, text="Ejecutar método", command=ejecutar_metodo).grid(row=4, column=0, columnspan=2, pady=10)

# --- Crear la tabla para mostrar los resultados de cada iteración ---
tabla = ttk.Treeview(ventana, columns=("Iteración", "r0", "r1", "Error"), show="headings", height=10)
tabla.heading("Iteración", text="Iteración")  # Encabezado para la columna de iteración
tabla.heading("r0", text="Valor Inicial (r0)")  # Encabezado para la columna de r0
tabla.heading("r1", text="Raíz Aproximada (r1)")  # Encabezado para la columna de r1
tabla.heading("Error", text="Error Absoluto")  # Encabezado para la columna de error
tabla.grid(row=5, column=0, columnspan=2, padx=10, pady=10)  # Posicionamos la tabla en la ventana

# Iniciamos el bucle de la interfaz gráfica
ventana.mainloop()