class Persona:
    #Atributos
    def __init__(self, nombre):
        self.nombre = nombre
        
    #Metodos
    def saludar(self):
            #Imprimiendo mensaje
            # #Formato convencional
            # print("Hola,soy", self.nombre)
            
            # #Formato con f string
            # print(f"Hola,soy, {self.nombre}")
            
            #Retornando mensaje
            return f"hola,soy {self.nombre}"

#Forma 1
persona1 = Persona("Hugo")
persona1.saludar()

#Forma 2
mensaje = persona1.saludar()
print(mensaje)