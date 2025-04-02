class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def saludar(self):  # Método
        return f"¡Hola, mi nombre es {self.nombre} y tengo {self.edad} años!"

# Instanciación de objetos
persona1 = Persona("Juan", 30)
persona2 = Persona("Ana", 25)

# Llamada al método
print(persona1.saludar())  # Llamamos al método 'saludar' de persona1
print(persona2.saludar())  # Llamamos al método 'saludar' de persona2
