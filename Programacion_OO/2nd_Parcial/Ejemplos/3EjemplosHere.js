// Clase base: Vehículo
class Vehículo {
    constructor(marca, modelo, año) {
        this.marca = marca;
        this.modelo = modelo;
        this.año = año;
    }

    detalles() {
        return `${this.marca} ${this.modelo} (${this.año})`;
    }
}

// Subclase: Bicicleta Eléctrica
class BicicletaEléctrica extends Vehículo {
    constructor(marca, modelo, año, autonomía) {
        super(marca, modelo, año);
        this.autonomía = autonomía;
    }

    cargarBatería() {
        return `Cargando la batería de la ${this.modelo}, autonomía: ${this.autonomía} km.`;
    }
}

// Clase base: Dispositivo Inteligente
class DispositivoInteligente {
    constructor(nombre, marca) {
        this.nombre = nombre;
        this.marca = marca;
        this.estado = "apagado";
    }

    encender() {
        this.estado = "encendido";
        return `${this.nombre} de ${this.marca} está ${this.estado}.`;
    }

    apagar() {
        this.estado = "apagado";
        return `${this.nombre} de ${this.marca} está ${this.estado}.`;
    }
}

// Subclase: Refrigerador Inteligente
class RefrigeradorInteligente extends DispositivoInteligente {
    constructor(nombre, marca, temperatura) {
        super(nombre, marca);
        this.temperatura = temperatura;
    }

    ajustarTemperatura(nuevaTemp) {
        this.temperatura = nuevaTemp;
        return `Temperatura del ${this.nombre} ajustada a ${this.temperatura}°C.`;
    }
}

// Clase base: Empleado
class Empleado {
    constructor(nombre, salario) {
        this.nombre = nombre;
        this.salario = salario;
    }

    obtenerSalario() {
        return `${this.nombre} tiene un salario de $${this.salario} USD.`;
    }
}

// Subclase: Desarrollador de Software
class DesarrolladorSoftware extends Empleado {
    constructor(nombre, salario, lenguaje) {
        super(nombre, salario);
        this.lenguaje = lenguaje;
    }

    escribirCódigo() {
        return `${this.nombre} está programando en ${this.lenguaje}.`;
    }
}

const bici = new BicicletaEléctrica("Xiaomi", "Mi Electric Scooter", 2023, 45);
console.log(bici.detalles());
console.log(bici.cargarBatería());

const refri = new RefrigeradorInteligente("Samsung Family Hub", "Samsung", 4);
console.log(refri.encender());
console.log(refri.ajustarTemperatura(2));

const dev = new DesarrolladorSoftware("Ana", 5000, "JavaScript");
console.log(dev.obtenerSalario());
console.log(dev.escribirCódigo());
