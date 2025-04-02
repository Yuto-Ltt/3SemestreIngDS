class Vigilancia {
    static totalAlumnos = 0;  
    constructor(nombre) {
        this.nombre = nombre;
        Vigilancia.totalAlumnos++;
        
    }
    mostrarDatos() {
        return `Alumno: ${this.nombre}`;
    }
    static obtenerTotalAlumnos() {
        return `Total de alumnos en el área de vigilancia: ${Vigilancia.totalAlumnos}`;
    }
}
// Registro de alumnos en vigilancia
const alumno1 = new Vigilancia("Melqui");   
const alumno2 = new Vigilancia("Zipur");  
const alumno3 = new Vigilancia("Jair");  
const alumno4 = new Vigilancia("Angel");  


console.log(alumno1.mostrarDatos()); 
console.log(alumno2.mostrarDatos()); 
console.log(alumno3.mostrarDatos()); 
console.log(alumno4.mostrarDatos()); 

console.log(Vigilancia.obtenerTotalAlumnos());
