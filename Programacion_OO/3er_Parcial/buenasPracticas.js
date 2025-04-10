class CocheDeportivo {
    /**
     * Representa un coche deportivo con marca, modelo y velocidad máxima.
     * @param {string} marca - Marca del coche deportivo.
     * @param {string} modelo - Modelo del coche deportivo.
     * @param {number} velocidadMaxima - Velocidad máxima del coche en km/h.
     */
    constructor(marca, modelo, velocidadMaxima) {
        this.marca = marca; // Marca del coche
        this.modelo = modelo; // Modelo del coche
        this.velocidadMaxima = velocidadMaxima; // Velocidad máxima
        this.velocidadActual = 0; // Velocidad actual
    }

    /**
     * Acelera el coche en una cantidad específica sin superar la velocidad máxima.
     * @param {number} cantidad - Cantidad de km/h a acelerar.
     */
    acelerar(cantidad) {
        if (cantidad > 0) {
            this.velocidadActual = Math.min(this.velocidadActual + cantidad, this.velocidadMaxima);
        } else {
            throw new Error("La cantidad de aceleración debe ser positiva.");
        }
    }

    /**
     * Reduce la velocidad del coche sin que sea menor a 0 km/h.
     * @param {number} cantidad - Cantidad de km/h a frenar.
     */
    frenar(cantidad) {
        if (cantidad > 0) {
            this.velocidadActual = Math.max(this.velocidadActual - cantidad, 0);
        } else {
            throw new Error("La cantidad de frenado debe ser positiva.");
        }
    }

    /**
     * Devuelve la velocidad actual del coche.
     * @returns {number} - Velocidad actual en km/h.
     */
    obtenerVelocidadActual() {
        return this.velocidadActual;
    }

    /**
     * Devuelve una representación en string del coche deportivo.
     * @returns {string}
     */
    toString() {
        return `Coche Deportivo: ${this.marca} ${this.modelo}, Velocidad Máxima: ${this.velocidadMaxima} km/h, Velocidad Actual: ${this.velocidadActual} km/h`;
    }
}

// Ejemplo de uso
const ferrari = new CocheDeportivo("Ferrari", "488 GTB", 330);
ferrari.acelerar(100);
ferrari.frenar(30);
console.log(ferrari.toString());
