class Persona{
    static contador = 0;
    constructor(nombre, edad){
        this.nombre = nombre;
        this.edad = edad;
        Persona.contador ++;
    }
    mostarInformacion(){
        return `nombre: ${this.nombre}, edad: ${this.edad}`
    }
    static obtenerTotalPersonas(){
        return Persona.contador;
    }
}

// Creacion de objeto persona 1
const persona1 = new Persona("Hugo", 19);
console.log(persona1.mostarInformacion());
//Metodo estatico
console.log(Persona.obtenerTotalPersonas());
