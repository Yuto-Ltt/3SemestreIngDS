class Animal:
    def __init__(self, salvaje):
        self.salvaje = salvaje
    
    def saludar(self):
        return f"{self.salvaje}, es un animal salvaje"
 
animal1 = Animal("Leon")
mensaje = animal1.saludar()
print(mensaje)