# Definimos clase 
class Coche:
    # Definimos atributos
    def __init__(self, modelo, color):
        self.modelo = modelo
        self.color = color   

    # Definimos métodos
    def describir(self):
        print(f"Este es un coche {self.color} de modelo {self.modelo}.")

# Definimos objeto coche
coche1 = Coche("Nissan Skyline R34", "Gris con líneas Azules")
coche2 = Coche("Dodge Charger", "Negro")
coche1.describir()
coche2.describir()

# Definimos clase 
class Playa:
    # Definimos atributos
    def __init__(self, lugar, puntuacion):
        self.lugar = lugar
        self.puntuacion = puntuacion

    # Definimos métodos    
    def describir(self):
        print(f"Esta playa ubicada en {self.lugar}, me gusta un {self.puntuacion}.")

# Definimos objeto playa
playa1 = Playa("Cancún", "9 de 10")
playa2 = Playa("Pueto Vayarta", "7 de 10")
playa1.describir()
playa2.describir()

# Definimos clase 
class Celular:
    # Definimos atributos
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo 

    # Definimos métodos     
    def describir(self):
        print(f"Este celular es un {self.modelo}, de la compañía {self.marca}.")

# Definimos objeto celular
celular1 = Celular("Iphone 16", "Apple")
celular2 = Celular("Xiaomi 14", "Xiaomi")
celular1.describir()
celular2.describir()