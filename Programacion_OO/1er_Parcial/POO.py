class Animal:
    def __init__(self, salvaje):
        self.salvaje = salvaje
    
    def mostrar_caracteristica(self):
        return f"{self.salvaje} es un animal territorial"

animal1 = Animal("León")
print(animal1.mostrar_caracteristica())
