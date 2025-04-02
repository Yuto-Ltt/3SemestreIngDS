# Definición de la clase
class Persona:
    def __init__(self, nombre, edad, ciudad):
        self.nombre = nombre  # Atributo
        self.edad = edad      # Atributo
        self.ciudad = ciudad  # Atributo

    def saludar(self):  # Método
        return f"¡Hola, mi nombre es {self.nombre}, tengo {self.edad} años y vivo en {self.ciudad}!"

    def cumplir_anios(self):  # Método
        self.edad += 1  # Modificando el atributo 'edad'
        return f"Ahora tengo {self.edad} años."

# Instanciación de objetos (Creando instancias de la clase Persona)
persona1 = Persona("Juan", 30, "Madrid")  # Objeto de la clase Persona
persona2 = Persona("Ana", 25, "Barcelona")  # Objeto de la clase Persona

# Llamada a métodos y acceso a atributos
print(persona1.saludar())  # Llamamos al método 'saludar' de persona1
print(persona2.saludar())  # Llamamos al método 'saludar' de persona2

# Cambiar atributo 'edad' de persona1
print(persona1.cumplir_anios())  # Llamamos al método 'cumplir_anios' de persona1
