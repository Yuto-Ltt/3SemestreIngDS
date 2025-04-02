class Autor {
    constructor(nombre, apellidos) {
        this.nombre = this.validarTexto(nombre, "El nombre no puede estar vacio");
        this.apellidos = this.validarTexto(apellidos, "Los apellidos no pueden estar vacios");
    }
    
    validarTexto(valor, mensaje) {
        if (!valor.trim()) throw new Error(mensaje);
        return valor.trim();
    }
    
    mostrarAutor() {
        return `${this.nombre} ${this.apellidos}`;
    }
}

class Libro {
    constructor(titulo, isbn, autor) {
        this.titulo = this.validarTexto(titulo, "El titulo no puede estar vacio");
        this.isbn = this.validarTexto(isbn, "El ISBN no puede estar vacio");
        if (!(autor instanceof Autor)) throw new Error("El autor debe ser una instancia valida de Autor");
        this.autor = autor;
    }
    
    validarTexto(valor, mensaje) {
        if (!valor.trim()) throw new Error(mensaje);
        return valor.trim();
    }
    
    mostrarLibro() {
        return `Titulo: ${this.titulo}, ISBN: ${this.isbn}, Autor: ${this.autor.mostrarAutor()}`;
    }
}

class Articulo extends Libro {
    constructor(titulo, isbn, autor, nombreRevista) {
        super(titulo, isbn, autor);
        this.nombreRevista = this.validarTexto(nombreRevista, "El nombre de la revista no puede estar vacio");
    }
    
    mostrarLibro() {
        return `${super.mostrarLibro()}, Revista: ${this.nombreRevista}`;
    }
}

class Biblioteca {
    constructor() {
        this.listaLibros = [];
    }
    
    agregarLibro(libro) {
        if (!(libro instanceof Libro)) throw new Error("Debe ser una instancia válida de Libro o Articulo");
        this.listaLibros.push(libro);
    }
    
    mostrarBiblioteca() {
        return this.listaLibros.length ? this.listaLibros.map(libro => libro.mostrarLibro()).join('\n') : "La biblioteca está vacía.";
    }
    
    borrarLibro(titulo) {
        const index = this.listaLibros.findIndex(libro => libro.titulo === titulo);
        if (index === -1) throw new Error("Libro no encontrado");
        this.listaLibros.splice(index, 1);
    }
    
    contarLibros() {
        return this.listaLibros.length;
    }
}

function pedirDatos(mensaje) {
    return prompt(mensaje).trim();
}

function menu() {
    const biblioteca = new Biblioteca();
    let opcion;
    do {
        opcion = pedirDatos(`Mene:\n1. Agregar libro\n2. Agregar artículo\n3. Mostrar biblioteca\n4. Borrar libro/articulo\n5. Consultar numero de libros/artículos\n6. Salir`);
        try {
            if (opcion === '1' || opcion === '2') {
                const titulo = pedirDatos("Título:");
                const isbn = pedirDatos("ISBN:");
                const autor = new Autor(pedirDatos("Autor (Nombre):"), pedirDatos("Autor (Apellidos):"));
                const libro = opcion === '1' ? new Libro(titulo, isbn, autor) : new Articulo(titulo, isbn, autor, pedirDatos("Nombre de la revista:"));
                biblioteca.agregarLibro(libro);
                console.log("Elemento agregado exitosamente.");
            } else if (opcion === '3') {
                console.log(biblioteca.mostrarBiblioteca());
            } else if (opcion === '4') {
                biblioteca.borrarLibro(pedirDatos("Titulo del libro/articulo a borrar:"));
                console.log("Libro eliminado exitosamente.");
            } else if (opcion === '5') {
                console.log(`Numero de libros/articulos: ${biblioteca.contarLibros()}`);
            } else if (opcion !== '6') {
                console.log("Opcion no valida, intente de nuevo.");
            }
        } catch (error) {
            console.log(`Error: ${error.message}`);
        }
    } while (opcion !== '6');
}

menu();
