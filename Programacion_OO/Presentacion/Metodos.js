class Persona {
    constructor(nombre, edad) {
        this.nombre = nombre;
        this.edad = edad;
    }

    saludar() {  // Método
        return `¡Hola, mi nombre es ${this.nombre} y tengo ${this.edad} años!`;
    }
}

// Instanciación de objetos
const persona1 = new Persona("Juan", 30);
const persona2 = new Persona("Ana", 25);

// Llamada al método
console.log(persona1.saludar());  // Llamamos al método 'saludar' de persona1
console.log(persona2.saludar());  // Llamamos al método 'saludar' de persona2
