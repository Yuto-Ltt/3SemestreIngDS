// Superclase (Clase Padre)
class Animal {
    constructor(nombre) {
        this.nombre = nombre;
    }

    // Método de la superclase
    hacerSonido() {
        console.log("El animal hace un sonido.");
    }
}

// Subclase Perro que hereda de Animal
class Perro extends Animal {
    constructor(nombre, raza) {
        super(nombre); // Llama al constructor de la superclase
        this.raza = raza;
    }

    // Método específico de Perro
    ladrar() {
        console.log(`${this.nombre} está ladrando: ¡Guau, guau!`);
    }
}

// Subclase Gato que hereda de Animal
class Gato extends Animal {
    constructor(nombre, color) {
        super(nombre);
        this.color = color;
    }

    // Método específico de Gato
    maullar() {
        console.log(`${this.nombre} está maullando: ¡Miau, miau!`);
    }
}

// Crear instancias
const miPerro = new Perro("Rex", "Labrador");
const miGato = new Gato("Michi", "Blanco");

// Llamar métodos heredados y propios
miPerro.hacerSonido(); // "El animal hace un sonido."
miPerro.ladrar();      // "Rex está ladrando: ¡Guau, guau!"

miGato.hacerSonido(); // "El animal hace un sonido."
miGato.maullar();     // "Michi está maullando: ¡Miau, miau!"
