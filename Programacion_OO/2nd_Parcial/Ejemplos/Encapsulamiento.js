class Rectangulo {
    #largo;
    #ancho;
    
    constructor(largo, ancho) {
      this.largo = largo; 
      this.ancho = ancho; 
    }
  
    get largo() {
      return this.#largo;
    }
  
    set largo(largo) {
      if (largo <= 0) {
        throw new Error(`El largo (${largo}) debe ser mayor que 0`);
      }
      this.#largo = largo;
    }
  
    get ancho() {
      return this.#ancho;
    }
  
    set ancho(ancho) {
      if (ancho <= 0) {
        throw new Error(`El ancho (${ancho}) debe ser mayor que 0`);
      }
      this.#ancho = ancho;
    }
  
    calcularArea() {
      return this.#largo * this.#ancho;
    }
  
    calcularPerimetro() {
      return 2 * (this.#largo + this.#ancho);
    }
  }
  
  try {
    const rectangulo = new Rectangulo(10, 7);
    console.log(`Area: ${rectangulo.calcularArea()}`);
    console.log(`Perimetro: ${rectangulo.calcularPerimetro()}`);
  
    rectangulo.largo = 6;
    rectangulo.ancho = 5;
    console.log(`Nueva Area: ${rectangulo.calcularArea()}`);
    console.log(`Nuevo Perimetro: ${rectangulo.calcularPerimetro()}`);
  
    try {
      rectangulo.largo = -2;
    } catch (error) {
      console.error("Error al establecer el largo:", error.message);
    }
  } catch (error) {
    console.error("Error al crear rectángulo:", error.message);
  }
  