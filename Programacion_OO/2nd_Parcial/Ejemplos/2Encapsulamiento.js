class Circulo {
    #radio; // Propiedad privada 

    // Constructor 
    constructor(radio) {
        this.radio = radio; 
    }

    // Getter para obtener el valor del radio
    get radio() {
        return this.#radio;
    }

    // Setter para validar y asignar el nuevo radio
    set radio(nuevoRadio) {
        if (typeof nuevoRadio !== "number" || nuevoRadio <= 0) {
            throw new Error("El radio debe ser un número mayor que 0"); // Lanza un error si el valor no es válido
        }
        this.#radio = nuevoRadio; // Asigna el nuevo valor si es válido
    }

    // Getter para calcular y devolver el diámetro del círculo
    get diametro() {
        return this.#radio * 2;
    }

    // Getter para calcular y devolver el área del círculo
    get area() {
        return Math.PI * this.#radio ** 2;
    }

    // Getter para calcular y devolver el perímetro (circunferencia) del círculo
    get perimetro() {
        return 2 * Math.PI * this.#radio;
    }
}

// Bloque try-catch para manejar errores
try {
    // Crear una instancia de Circulo con radio 
    const circulo = new Circulo(5);
    console.log(`Radio: ${circulo.radio}`);
    console.log(`Diametro: ${circulo.diametro}`);
    console.log(`Area: ${circulo.area.toFixed(2)}`); // Redondeamos a 2 decimales
    console.log(`Perimetro: ${circulo.perimetro.toFixed(2)}`);

    // Modificar el radio y mostrar los nuevos valores
    circulo.radio = 5; 
    console.log(`\nNuevo Radio: ${circulo.radio}`);
    console.log(`Nuevo Diametro: ${circulo.diametro}`);
    console.log(`Nueva Area: ${circulo.area.toFixed(2)}`);
    console.log(`Nuevo Perimetro: ${circulo.perimetro.toFixed(2)}`);

    // Intentar asignar un radio inválido, lo que provocará un error
    circulo.radio = -3; 
} catch (error) {
    console.error("Error:", error.message); // Muestra el error en la consola
}
