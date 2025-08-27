CREATE TABLE IF NOT EXISTS nacionalidad(
    id_nacionalidad INT NOT NULL AUTO_INCREMENT,
    pais VARCHAR(50) NOT NULL,
    nacionalidad VARCHAR(50) NOT NULL,
    CONSTRAINT pk_nacionalidad PRIMARY KEY (id_nacionalidad)
);

CREATE TABLE IF NOT EXISTS autor(
    id_autor INT NOT NULL AUTO_INCREMENT,
    nombre_autor VARCHAR(100) NOT NULL,
    pseudonimo VARCHAR(100) NULL,
    id_nacionalidad INT NULL,
    habilitado TINYINT DEFAULT = 1,
    CONSTRAINT pk_autor PRIMARY KEY (id_autor),
    CONSTRAINT fk_autor_nacionalidad FOREIGN KEY (id_nacionalidad) REFERENCES nacionalidad(id_nacionalidad)
);

CREATE TABLE IF NOT EXISTS categoria(
    id_categoria INT NOT NULL AUTO_INCREMENT,
    categoria VARCHAR(50) NOT NULL,
    descripcion_c VARCHAR(255) NULL,
    CONSTRAINT pk_categoria PRIMARY KEY (id_categoria)
);

CREATE TABLE IF NOT EXISTS comuna(
    id_comuna INT NOT NULL AUTO_INCREMENT,
    cod_comuna VARCHAR(5) NOT NULL,
    nombre_comuna VARCHAR(50) NOT NULL,
    CONSTRAINT pk_comuna PRIMARY KEY (id_comuna)
);

CREATE TABLE IF NOT EXISTS direccion(
    id_direccion INT NOT NULL AUTO_INCREMENT,
    id_comuna INT NOT NULL,
    calle VARCHAR(100) NOT NULL,
    numero_d VARCHAR(10) NULL,
    departamento VARCHAR(10) NULL,
    CONSTRAINT pk_direccion PRIMARY KEY (id_direccion),
    CONSTRAINT fk_direccion_comuna FOREIGN KEY (id_comuna) REFERENCES comuna(id_comuna)
);

CREATE TABLE IF NOT EXISTS biblioteca(
    id_biblioteca INT NOT NULL AUTO_INCREMENT,
    nombre_biblio VARCHAR(100) NOT NULL,
    id_direccion INT NOT NULL,
    habilitado TINYINT DEFAULT = 1,
    CONSTRAINT pk_biblioteca PRIMARY KEY (id_biblioteca),
    CONSTRAINT fk_biblioteca_direccion FOREIGN KEY (id_direccion) REFERENCES direccion(id_direccion)
);

CREATE TABLE IF NOT EXISTS libro(
    id_libro INT NOT NULL AUTO_INCREMENT,
    titulo_libro VARCHAR(255) NOT NULL,
    id_autor INT NOT NULL,
    paginas INT NOT NULL,
    copias_libro INT NOT NULL,
    id_biblioteca INT NOT NULL,
    habilitado_libro TINYINT DEFAULT = 1,
    id_categoria INT NOT NULL,
    CONSTRAINT pk_libro PRIMARY KEY (id_libro),
    CONSTRAINT fk_libro_biblioteca FOREIGN KEY (id_biblioteca) REFERENCES biblioteca(id_biblioteca),
    CONSTRAINT fk_libro_categoria FOREIGN KEY (id_categoria) REFERENCES categoria(id_categoria)
);

CREATE TABLE IF NOT EXISTS lector(
    id_lector INT NOT NULL AUTO_INCREMENT,
    rut_lector INT NOT NULL,
    digito_verificador VARCHAR(1) NOT NULL,
    nombre_lector VARCHAR(255) NOT NULL,
    correo_lector VARCHAR(255) NOT NULL,
    telefono_lector VARCHAR(15) NOT NULL,
    id_direccion INT NOT NULL,
    id_biblioteca INT NOT NULL,
    habilitado_lector TINYINT DEFAULT = 1,
    CONSTRAINT pk_lector PRIMARY KEY (id_lector),
    CONSTRAINT fk_lector_direccion FOREIGN KEY (id_direccion) REFERENCES direccion(id_direccion),
    CONSTRAINT fk_lector_biblioteca FOREIGN KEY (id_biblioteca) REFERENCES biblioteca(id_biblioteca)
);

CREATE TABLE IF NOT EXISTS prestamo(
    id_prestamo INT NOT NULL,
    id_libro INT NOT NULL,
    id_lector INT NOT NULL,
    fecha_prestamo DATE NOT NULL,
    plazo_devolucion INT NOT NULL,
    fecha_entrega DATE NOT NULL,
    CONSTRAINT pk_prestamo PRIMARY KEY (id_prestamo),
    CONSTRAINT fk_prestamo_libro FOREIGN KEY (id_libro) REFERENCES libro(id_libro),
    CONSTRAINT fk_prestamo_lector FOREIGN KEY (id_lector) REFERENCES lector(id_lector)
);