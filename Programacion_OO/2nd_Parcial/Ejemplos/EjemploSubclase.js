class Autos{
    constructor(deportivo){
        this.deportivo = deportivo;
    }
    velocidad(){
        console.log(`El auto deportivo mas veloz es ${this.deportivo}`)
    }
}

class Modelo extends Autos{
    constructor(deportivo, marca){
        super(deportivo);
        this.marca = marca;
    }
    velocidad(){
        super.velocidad();
        console.log(`el ${this.deportivo} es un auto deportivo de la marca ${this.marca}`)
    }
}

const auto1 = new Modelo("Bugatti Chiron Super Sport 300+","Volkswagen" )
auto1.velocidad();