// Simulando una interfaz
class IConducible {
    drive() {
      throw new Error("El método 'drive' debe ser implementado");
    }
  }
  
  class Car extends IConducible {
    drive() {
      console.log("Conduciendo el coche");
    }
  }
  
  class Bike extends IConducible {
    drive() {
      console.log("Conduciendo la bicicleta");
    }
  }
  
  const car = new Car();
  car.drive(); // Conduciendo el coche
  
  const bike = new Bike();
  bike.drive(); // Conduciendo la bicicleta
  
  // Intento de crear una clase que no implemente la interfaz
  // class Boat extends IConducible {} // Error: El método 'drive' debe ser implementado
  