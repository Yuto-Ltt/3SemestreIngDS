// Simulando una clase abstracta
class Animal {
    constructor(name) {
      if (this.constructor === Animal) {
        throw new Error("No se puede instanciar una clase abstracta");
      }
      this.name = name;
    }
  
    // Método abstracto simulado
    makeSound() {
      throw new Error("El método 'makeSound' debe ser implementado");
    }
  }
  
  class Dog extends Animal {
    makeSound() {
      console.log(`${this.name} dice: ¡Guau!`);
    }
  }
  
  class Cat extends Animal {
    makeSound() {
      console.log(`${this.name} dice: ¡Miau!`);
    }
  }
  
  // Crear instancias
  const dog = new Dog('Rex');
  dog.makeSound(); // Rex dice: ¡Guau!
  
  const cat = new Cat('Whiskers');
  cat.makeSound(); // Whiskers dice: ¡Miau!
  
  // Intento de instanciar la clase abstracta
  // const animal = new Animal('Animal'); // Error: No se puede instanciar una clase abstracta
  