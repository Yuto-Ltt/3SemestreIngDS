import random

def adivinar_numero():
    print("¡Bienvenido al juego de Adivina el número!")
    print("Estoy pensando en un número entre 1 y 100.")
    
    # El número aleatorio que el programa elige
    numero_secreto = random.randint(1, 100)
    
    intentos = 0
    adivinado = False
    
    while not adivinado:
        # El jugador ingresa su suposición
        try:
            adivinanza = int(input("Ingresa tu suposición: "))
        except ValueError:
            print("Por favor, ingresa un número válido.")
            continue
        
        intentos += 1
        
        if adivinanza < numero_secreto:
            print("¡El número es más grande!")
        elif adivinanza > numero_secreto:
            print("¡El número es más pequeño!")
        else:
            adivinado = True
            print(f"¡Felicidades! Has adivinado el número en {intentos} intentos.")
    
if __name__ == "__main__":
    adivinar_numero()
