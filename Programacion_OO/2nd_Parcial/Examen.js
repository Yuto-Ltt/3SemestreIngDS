class Autor {
    #nombre;
    #apellidos;
    
    constructor(nombre, apellidos) {
        this.nombre = nombre;
        this.apellidos = apellidos;
    }
    
    set nombre(valor) {
        if (!valor.trim()) throw new Error("El nombre no puede estar vacío");
        this.#nombre = valor.trim();
    }
    
    set apellidos(valor) {
        if (!valor.trim()) throw new Error("Los apellidos no pueden estar vacíos");
        this.#apellidos = valor.trim();
    }
    
    get nombre() { return this.#nombre; }
    get apellidos() { return this.#apellidos; }
    
    mostrarAutor() {
        return `${this.#nombre} ${this.#apellidos}`;
    }
}

class Libro {
    #titulo;
    #isbn;
    #autor;
    
    constructor(titulo, isbn, autor) {
        this.titulo = titulo;
        this.isbn = isbn;
        this.agregarAutor(autor);
    }
    
    set titulo(valor) {
        if (!valor.trim()) throw new Error("El título no puede estar vacío");
        this.#titulo = valor.trim();
    }
    
    set isbn(valor) {
        if (!valor.trim()) throw new Error("El ISBN no puede estar vacío");
        this.#isbn = valor.trim();
    }
    
    get titulo() { return this.#titulo; }
    get isbn() { return this.#isbn; }
    
    agregarAutor(autor) {
        if (!(autor instanceof Autor)) throw new Error("El autor debe ser una instancia válida de Autor");
        this.#autor = autor;
    }
    
    mostrarLibro() {
        return `Título: ${this.#titulo}, ISBN: ${this.#isbn}, Autor: ${this.#autor.mostrarAutor()}`;
    }
}

class Articulo extends Libro {
    #nombreRevista;
    
    constructor(titulo, isbn, autor, nombreRevista) {
        super(titulo, isbn, autor);
        this.nombreRevista = nombreRevista;
    }
    
    set nombreRevista(valor) {
        if (!valor.trim()) throw new Error("El nombre de la revista no puede estar vacío");
        this.#nombreRevista = valor.trim();
    }
    
    get nombreRevista() { return this.#nombreRevista; }
    
    mostrarLibro() {
        return `${super.mostrarLibro()}, Revista: ${this.#nombreRevista}`;
    }
}

class Biblioteca {
    #listaLibros = [];
    
    agregarLibro(libro) {
        if (!(libro instanceof Libro)) throw new Error("Debe ser una instancia válida de Libro o Articulo");
        this.#listaLibros.push(libro);
    }
    
    mostrarBiblioteca() {
        if (this.#listaLibros.length === 0) return "La biblioteca está vacía.";
        return this.#listaLibros.map(libro => libro.mostrarLibro()).join('\n');
    }
    
    borrarLibro(titulo) {
        const index = this.#listaLibros.findIndex(libro => libro.titulo === titulo);
        if (index === -1) throw new Error("Libro no encontrado");
        this.#listaLibros.splice(index, 1);
    }
    
    contarLibros() {
        return this.#listaLibros.length;
    }
}

function menu() {
    const biblioteca = new Biblioteca();
    let opcion;
    do {
        opcion = prompt(`Menú:\n1. Agregar libro\n2. Agregar artículo\n3. Mostrar biblioteca\n4. Borrar libro/artículo\n5. Consultar número de libros/artículos\n6. Salir`);
        try {
            switch (opcion) {
                case '1': {
                    const titulo = prompt("Título:");
                    const isbn = prompt("ISBN:");
                    const nombre = prompt("Autor (Nombre):");
                    const apellidos = prompt("Autor (Apellidos):");
                    const autor = new Autor(nombre, apellidos);
                    biblioteca.agregarLibro(new Libro(titulo, isbn, autor));
                    console.log("Libro agregado exitosamente.");
                    break;
                }
                case '2': {
                    const titulo = prompt("Título:");
                    const isbn = prompt("ISBN:");
                    const nombre = prompt("Autor (Nombre):");
                    const apellidos = prompt("Autor (Apellidos):");
                    const nombreRevista = prompt("Nombre de la revista:");
                    const autor = new Autor(nombre, apellidos);
                    biblioteca.agregarLibro(new Articulo(titulo, isbn, autor, nombreRevista));
                    console.log("Artículo agregado exitosamente.");
                    break;
                }
                case '3':
                    console.log(biblioteca.mostrarBiblioteca());
                    break;
                case '4': {
                    const titulo = prompt("Título del libro/artículo a borrar:");
                    biblioteca.borrarLibro(titulo);
                    console.log("Libro eliminado exitosamente.");
                    break;
                }
                case '5':
                    console.log(`Número de libros/artículos: ${biblioteca.contarLibros()}`);
                    break;
                case '6':
                    console.log("Saliendo...");
                    break;
                default:
                    console.log("Opción no válida, intente de nuevo.");
            }
        } catch (error) {
            console.log(`Error: ${error.message}`);
        }
    } while (opcion !== '6');
}

menu();
