# Definimos clase
class Coche:
# Definimos atributos
    def __init__(self, modelo, color):
        self.modelo = modelo
        self.color = color   
# Definimos metodos
    def describir(self):
        print(f"Este es un coche {self.color} de modelo {self.modelo}.")
# Definimos objeto
coche1 = Coche("Nissan Skyline R34", "Gris con lineas Azules")
coche1.describir()