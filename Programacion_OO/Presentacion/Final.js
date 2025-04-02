// Definición de la clase
class Persona {
    constructor(nombre, edad, ciudad) {
        this.nombre = nombre;  // Atributo
        this.edad = edad;      // Atributo
        this.ciudad = ciudad;  // Atributo
    }

    // Método
    saludar() {
        return `¡Hola, mi nombre es ${this.nombre}, tengo ${this.edad} años y vivo en ${this.ciudad}!`;
    }

    // Método
    cumplirAnios() {
        this.edad += 1;  // Modificando el atributo 'edad'
        return `Ahora tengo ${this.edad} años.`;
    }
}

// Instanciación de objetos (Creando instancias de la clase Persona)
const persona1 = new Persona("Juan", 30, "Madrid");  // Objeto de la clase Persona
const persona2 = new Persona("Ana", 25, "Barcelona");  // Objeto de la clase Persona

// Llamada a métodos y acceso a atributos
console.log(persona1.saludar());  // Llamamos al método 'saludar' de persona1
console.log(persona2.saludar());  // Llamamos al método 'saludar' de persona2

// Cambiar atributo 'edad' de persona1
console.log(persona1.cumplirAnios());  // Llamamos al método 'cumplirAnios' de persona1
