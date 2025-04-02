class Autos {
    constructor(deportivo, velocidadMax) {
        this.deportivo = deportivo; 
        this.velocidadMax = velocidadMax; 
    }
    velocidad() {
        console.log(`El auto deportivo más veloz es ${this.deportivo} con una velocidad máxima de ${this.velocidadMax} km/h`);
    }
}

class Modelo extends Autos {
    constructor(deportivo, velocidadMax, marca, otrosModelos = []) {
        super(deportivo, velocidadMax); 
        this.marca = marca;
        this.otrosModelos = otrosModelos; 
    }
    agregarModelo(modelo, velocidadMax) {
        this.otrosModelos.push({ modelo, velocidadMax }); 
    }
    mostrarModelos() {
        super.velocidad();
        console.log(`Otros autos deportivos de la marca ${this.marca} son:`);
        this.otrosModelos.forEach((auto, index) => {
            console.log(`${index + 1}. ${auto.modelo} con una velocidad máxima de ${auto.velocidadMax} km/h`);
        });
    }
}

const auto1 = new Modelo("Bugatti Chiron Super Sport 300+", 490, "Bugatti");
auto1.agregarModelo("Bugatti La Voiture Noire", 420);
auto1.agregarModelo("Bugatti Veyron", 407);
auto1.agregarModelo("Bugatti Divo", 380);
auto1.mostrarModelos();

