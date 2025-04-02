// Clase base (simulación de abstracción)
class Animal {
    constructor(nombre) {
        if (this.constructor === Animal) {
            throw new Error("No se puede instanciar una clase abstracta");
        }
        this.nombre = nombre;
    }

    // Método abstracto (debe ser sobrescrito por subclases)
    hacerSonido() {
        throw new Error("Método hacerSonido() debe ser implementado");
    }

    // Método concreto
    dormir() {
        console.log(`${this.nombre} está durmiendo.`);
    }
}

// Subclase Perro
class Perro extends Animal {
    hacerSonido() {
        console.log(`${this.nombre} ladra: ¡Guau, guau!`);
    }
}

// Subclase Gato
class Gato extends Animal {
    hacerSonido() {
        console.log(`${this.nombre} maulla: ¡Miau, miau!`);
    }
}

// Crear instancias
const miPerro = new Perro("Rex");
const miGato = new Gato("Michi");

miPerro.hacerSonido(); // Rex ladra: ¡Guau, guau!
miPerro.dormir();      // Rex está durmiendo.

miGato.hacerSonido();  // Michi maulla: ¡Miau, miau!
miGato.dormir();       // Michi está durmiendo.
