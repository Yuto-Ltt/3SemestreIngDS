class Animal {
    constructor(salvaje) {
        this.salvaje = salvaje;
    }

    mostrarCaracteristica() {
        return `${this.salvaje} es un animal territorial`;
    }
}

const animal1 = new Animal("León");
console.log(animal1.mostrarCaracteristica());



