class CocheDeportivo {
    
    constructor(marca, modelo, velocidadMaxima) {
        this.marca = marca; // Marca del coche
        this.modelo = modelo; // Modelo del coche
        this.velocidadMaxima = velocidadMaxima; // Velocidad máxima
        this.velocidadActual = 0; // Velocidad actual
    }

    
    acelerar(cantidad) {
        if (cantidad > 0) {
            this.velocidadActual = Math.min(this.velocidadActual + cantidad, this.velocidadMaxima);
        } else {
            throw new Error("La cantidad de aceleración debe ser positiva.");
        }
    }

   
    frenar(cantidad) {
        if (cantidad > 0) {
            this.velocidadActual = Math.max(this.velocidadActual - cantidad, 0);
        } else {
            throw new Error("La cantidad de frenado debe ser positiva.");
        }
    }

    
    obtenerVelocidadActual() {
        return this.velocidadActual;
    }

    
    toString() {
        return `Coche Deportivo: ${this.marca} ${this.modelo}, Velocidad Máxima: ${this.velocidadMaxima} km/h, Velocidad Actual: ${this.velocidadActual} km/h`;
    }
}

// Ejemplo de uso
const ferrari = new CocheDeportivo("Ferrari", "488 GTB", 330);
ferrari.acelerar(100);
ferrari.frenar(30);
console.log(ferrari.toString());
