class Persona {
    // Propiedad privada
    _nombre;
  
    // Constructor
    constructor(nombre) {
      // Usamos el setter para asignar el valor inicial
      this.nombre = nombre; // Llama al setter que validará el valor
    }
  
    // Getter para acceder a la propiedad privada
    get nombre() {
      return this._nombre; // Retornar el nombre
    }
  
    // Setter para modificar la propiedad privada
    set nombre(nuevoNombre) {
      this._nombre = nuevoNombre; // Cambiar el valor del nombre
    }
  }
  
  // Ejemplo de uso

    // Crear una nueva persona
    const persona = new Persona("RONALD");
    console.log(persona.nombre); // Nombre: RONALD
  
    // Cambiar el nombre
  persona.nombre = "                Oswaldo";
  console.log(persona.nombre); // Nombre: Oswaldo


  class Persona {
    // Propiedad privada
    _nombre;
  
    // Constructor
    constructor(nombre) {
      // Usamos el setter para asignar el valor inicial
      this.nombre = nombre; // Llama al setter que validará el valor
    }
  
    // Getter para acceder a la propiedad privada
    get nombre() {
      return this._nombre; // Retornar el nombre
    }
  
    // Setter para modificar la propiedad privada con validación
    set nombre(nuevoNombre) {
      if (!nuevoNombre || nuevoNombre.trim() === "") {
        throw new Error("El nombre no puede estar vacío.");
      }
      this._nombre = nuevoNombre.trim().toUpperCase(); // Cambiar el valor del nombre si es válido. Elimina espacios y convierte a mayusculas
    }
  }
  
  // Ejemplo de uso
  
  try {
    // Crear una nueva persona con un nombre válido
    const persona = new Persona("Ronald");
    console.log(persona.nombre); // Nombre: RONALD
  
    // Cambiar el nombre a un valor válido
    persona._nombre = "      oswaldo";
    console.log(persona.nombre); // Nombre: OSWALDO
    
    // Intentar establecer un nombre vacío (esto generará un error)
    persona._nombre = "       ^      "; // Esto lanzará un Error: "El nombre no puede estar vacío."
    console.log(persona.nombre);

  } catch (error) {
    console.error(error.message); // Manejo del error
  }


  class Persona {
    // Uso de # a partir de ES2022
    // Propiedad privada
    #nombre;
  
    // Constructor
    constructor(nombre) {
      // Usamos el setter para asignar el valor inicial
      this.nombre = nombre; // Llama al setter que validará el valor
    }
  
    // Getter para acceder a la propiedad privada
    get nombre() {
      return this.#nombre; // Retornar el nombre
    }
  
    // Setter para modificar la propiedad privada con validación
    set nombre(nuevoNombre) {
      if (!nuevoNombre || nuevoNombre.trim() === "") {
        throw new Error("El nombre no puede estar vacío.");
      }
      this.#nombre = nuevoNombre.trim().toUpperCase(); // Cambiar el valor del nombre si es válido. Elimina espacios y convierte a mayusculas
    }
  }
  
  // Ejemplo de uso
  
  try {
    // Crear una nueva persona con un nombre válido
    const persona = new Persona("Ronald");
    console.log(persona.nombre); // Nombre: RONALD
  
    // Cambiar el nombre a un valor válido
    persona.nombre = "     oswaldo";
    console.log(persona.nombre); // Nombre: OSWALDO
  
    // Intentar establecer un nombre vacío (esto generará un error)
    persona.nombre = ""; // Esto lanzará un Error: "El nombre no puede estar vacío."
  
  } catch (error) {
    console.error(error.message); // Manejo del error
  }