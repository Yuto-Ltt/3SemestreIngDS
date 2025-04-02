# Definimos clase
class Alumnos:
     # Definimos constructor 
     def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
     #Definimos metodo
     def presentacion(self):
        return f'El alumno {self.nombre} tiene {self.edad} años'
#Creacion de instancias
alumno1 = Alumnos("itiel", 18)
#Ejecucion del metodo
print(alumno1.presentacion())        