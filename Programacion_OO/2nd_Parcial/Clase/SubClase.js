class Persona{
    constructor(nombre){
        this.nombre = nombre;
    }
    presentarse(){
        console.log (`Saquen los focoKrispis que ando bien erizo soy el ${this.nombre}`)
    }
}

class Alumno extends Persona{
    constructor(nombre, curso){
        super(nombre);
        this.curso = curso;
    }
    presentarse(){
        super.presentarse();
        console.log(`Estoy en mi zona paps la zona del ${this.curso}`)
    }
}

const alumno1 = new Alumno ("El Tijuano", "Chesco")
alumno1.presentarse();