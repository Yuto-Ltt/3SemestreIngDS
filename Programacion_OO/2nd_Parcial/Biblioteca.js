// Clase Autor para gestionar los autores
class Autor {
    // Propiedades privadas: nombre y apellidos
    #nombre;
    #apellidos;
    
    constructor(nombre, apellidos) {
        // Validacion de los valores al asignarlos
        this.nombre = nombre;
        this.apellidos = apellidos;
    }
    
    // Setter para el nombre, valida que no este vacío
    set nombre(valor) {
        // Aqui se valida que el valor no este vacio. Si está vacio o solo tiene espacios, lanzamos un error
        // Esto garantiza que el autor siempre tendra un nombre valido.
        if (!valor.trim()) throw new Error("El nombre no puede estar vacío");
        this.#nombre = valor.trim();
    }
    
    // Setter para los apellidos, valida que no esten vacios
    set apellidos(valor) {
        // Igual que en el setter de nombre, garantizamos que el valor no este vacio.
        if (!valor.trim()) throw new Error("Los apellidos no pueden estar vacíos");
        this.#apellidos = valor.trim();
    }
    
    // Getter para el nombre, simplemente devuelve el valor
    get nombre() { return this.#nombre; }
    
    // Getter para los apellidos, devuelve el valor
    get apellidos() { return this.#apellidos; }
    
    // Metodo para mostrar el nombre completo del autor
    mostrarAutor() {
        /* Aqui devolvemos el nombre completo del autor. Usamos la propiedad privada #nombre y #apellidos
        porque el acceso a estas propiedades está restringido, lo que asegura el uso controlado de los datos*/
        return `${this.#nombre} ${this.#apellidos}`;
    }
}

// Clase Libro que hereda características de Autor y gestiona libros
class Libro {
    // Propiedades privadas: titulo, ISBN y autor
    #titulo;
    #isbn;
    #autor;
    
    constructor(titulo, isbn, autor) {
        // Aquí se valida que tanto el titulo como el ISBN no esten vacios
        // Si alguno de estos datos está vacio, se lanza un error, lo que garantiza que
        // siempre tengamos datos completos y validos para el libro
        this.titulo = titulo;
        this.isbn = isbn;
        this.agregarAutor(autor); // Asignamos el autor utilizando un método
    }
    
    // Setter para el titulo, valida que no esté vacío
    set titulo(valor) {
        // Si el titulo está vacio o solo contiene espacios, se lanza un error
        // Esto asegura que el libro siempre tendrá un titulo valido
        if (!valor.trim()) throw new Error("El título no puede estar vacío");
        this.#titulo = valor.trim();
    }
    
    // Setter para el ISBN, valida que no esté vacío
    set isbn(valor) {
        // Aqui tambien se valida el ISBN para asegurarnos de que el libro tenga un identificador unico
        // que no este vacio ni contenga solo espacios
        if (!valor.trim()) throw new Error("El ISBN no puede estar vacío");
        this.#isbn = valor.trim();
    }
    
    // Getter para el titulo
    get titulo() { return this.#titulo; }
    
    // Getter para el ISBN
    get isbn() { return this.#isbn; }
    
    // Metodo para asignar un autor al libro
    agregarAutor(autor) {
        // Verificamos que el autor proporcionado sea una instancia de la clase Autor
        // Esto nos asegura que estamos asociando un objeto de autor válido al libro, 
        // previniendo errores si el autor no es adecuado
        if (!(autor instanceof Autor)) throw new Error("El autor debe ser una instancia válida de Autor");
        this.#autor = autor;
    }
    
    // Metodo para mostrar la información del libro
    mostrarLibro() {
        // Este metodo proporciona una representación del libro en formato texto
        // Usamos el método `mostrarAutor()` de la clase Autor para obtener el nombre del autor
        // y luego mostrarlo junto con el titulo y el ISBN del libro
        return `Título: ${this.#titulo}, ISBN: ${this.#isbn}, Autor: ${this.#autor.mostrarAutor()}`;
    }
}

// Clase Articulo que hereda de Libro, añadiendo la revista como especialización
class Articulo extends Libro {
    // Propiedad privada: nombre de la revista
    #nombreRevista;
    
    constructor(titulo, isbn, autor, nombreRevista) {
        super(titulo, isbn, autor); // Llamada al constructor de la clase base (Libro)
        this.nombreRevista = nombreRevista; // Asignación del nombre de la revista
    }
    
    // Setter para el nombre de la revista, valida que no esté vacío
    set nombreRevista(valor) {
        // Similar a la validación para titulo o ISBN, garantizamos que el nombre de la revista no este vacio
        if (!valor.trim()) throw new Error("El nombre de la revista no puede estar vacío");
        this.#nombreRevista = valor.trim();
    }
    
    // Getter para el nombre de la revista
    get nombreRevista() { return this.#nombreRevista; }
    
    // Metodo sobrescrito para mostrar la información del artículo, incluyendo la revista
    mostrarLibro() {
        // Sobrescribimos el método `mostrarLibro` para incluir información adicional: el nombre de la revista
        // Llamamos a `super.mostrarLibro()` para obtener la información base del libro
        // y luego le agregamos la revista
        return `${super.mostrarLibro()}, Revista: ${this.#nombreRevista}`;
    }
}

// Clase Biblioteca para gestionar una colección de libros y artículos
class Biblioteca {
    // Lista privada de libros y artículos
    #listaLibros = [];
    
    // Metodo para agregar un libro o artículo a la biblioteca
    agregarLibro(libro) {
        // Si el libro no es una instancia valida de la clase Libro o Articulo, se lanza un error
        // Esto previene que objetos no deseados se agreguen a la biblioteca
        if (!(libro instanceof Libro)) throw new Error("Debe ser una instancia valida de Libro o Articulo");
        this.#listaLibros.push(libro);
    }
    
    // Metodo para mostrar todos los libros/artículos en la biblioteca
    mostrarBiblioteca() {
        // Si no hay libros/artículos en la lista, devolvemos un mensaje indicando que la biblioteca esta vacia
        // De lo contrario, mostramos todos los libros/articulos, uno por uno
        if (this.#listaLibros.length === 0) return "La biblioteca está vacia.";
        return this.#listaLibros.map(libro => libro.mostrarLibro()).join('\n');
    }
    
    // Metodo para borrar un libro/artículo por su título
    borrarLibro(titulo) {
        // Buscamos el libro/articulo por su titulo en la lista. Si no lo encontramos, lanzamos un error.
        // Si lo encontramos, lo eliminamos de la lista.
        const index = this.#listaLibros.findIndex(libro => libro.titulo === titulo);
        if (index === -1) throw new Error("Libro no encontrado");
        this.#listaLibros.splice(index, 1);
    }
    
    // Metodo para contar la cantidad de libros/articulos en la biblioteca
    contarLibros() {
        // Este metodo simplemente devuelve la longitud de la lista de libros/artículos,
        // lo que nos da el número total de elementos en la biblioteca
        return this.#listaLibros.length;
    }
}

// Funcion principal que simula el menu para interactuar con la biblioteca
function menu() {
    const biblioteca = new Biblioteca(); // Creamos una nueva instancia de la biblioteca
    let opcion;
    
    do {
        // Mostramos el menu y obtenemos la opcion del usuario
        opcion = prompt(`Menú:\n1. Agregar libro\n2. Agregar artículo\n3. Mostrar biblioteca\n4. Borrar libro/artículo\n5. Consultar número de libros/artículos\n6. Salir`);
        
        try {
            // Segun la opcion elegida, realizamos una accion
            switch (opcion) {
                case '1': { // Opcion para agregar un libro
                    const titulo = prompt("Título:");
                    const isbn = prompt("ISBN:");
                    const nombre = prompt("Autor (Nombre):");
                    const apellidos = prompt("Autor (Apellidos):");
                    const autor = new Autor(nombre, apellidos); // Creamos un autor
                    biblioteca.agregarLibro(new Libro(titulo, isbn, autor)); // Agregamos el libro
                    console.log("Libro agregado exitosamente.");
                    break;
                }
                case '2': { // Opcion para agregar un artículo
                    const titulo = prompt("Título:");
                    const isbn = prompt("ISBN:");
                    const nombre = prompt("Autor (Nombre):");
                    const apellidos = prompt("Autor (Apellidos):");
                    const nombreRevista = prompt("Nombre de la revista:");
                    const autor = new Autor(nombre, apellidos); // Creamos un autor
                    biblioteca.agregarLibro(new Articulo(titulo, isbn, autor, nombreRevista)); // Agregamos el articulo
                    console.log("Artículo agregado exitosamente.");
                    break;
                }
                case '3': // Opcion para mostrar todos los libros/articulos
                    console.log(biblioteca.mostrarBiblioteca());
                    break;
                case '4': { // Opcion para borrar un libro/articulo por titulo
                    const titulo = prompt("Título del libro/artículo a borrar:");
                    biblioteca.borrarLibro(titulo); // Borramos el libro/articulo
                    console.log("Libro eliminado exitosamente.");
                    break;
                }
                case '5': // Opcion para consultar el número de libros/articulos
                    console.log(`Número de libros/artículos: ${biblioteca.contarLibros()}`);
                    break;
                case '6': // Opcion para salir
                    console.log("Saliendo...");
                    break;
                default:
                    console.log("Opción no válida, intente de nuevo.");
            }
        } catch (error) {
            // Captura y muestra los errores si ocurre algo inesperado
            console.log(`Error: ${error.message}`);
        }
    } while (opcion !== '6'); // El menu continuara hasta que el usuario elija salir
}

// Ejecutamos la funcion menu para iniciar el programa
menu();