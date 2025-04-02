class Persona {
    #nombre; // Propiedad privada

    constructor(nombre) {
        this.#nombre = nombre; // Solo accesible dentro de la clase
    }

    obtenerNombre() {
        return this.#nombre; // Método público para acceder
    }
}

const persona = new Persona("Hermenegildo");

console.log(persona.obtenerNombre()); 
console.log(persona.nombre); 
