//Definimos la clase
class salon{
//Definimos el constructor
    constructor(cantidad, edificio){
        this.cantidad = cantidad;
        this.edificio = edificio;
    }
//Definimos el metodo 
lugar(){
    retur`El edifico ${this.edificio} tiene ${this.cantidad} salones`;
}
}
//Creacion de la instancia
const edificio1 = newSalon (15, "B");
//Ejecutamos el metodo
console.log(edificio1.lugar());

