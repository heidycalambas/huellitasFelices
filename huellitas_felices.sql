CREATE DATABASE huellitas_felices;

USE huellitas_felices;

-- ==========================================
-- TABLA: USUARIOS
-- ==========================================

CREATE TABLE usuarios (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    edad INT NOT NULL,
    ciudad VARCHAR(100) NOT NULL,
    tipo_vivienda VARCHAR(50),
    tiene_patio BOOLEAN DEFAULT FALSE,
    otras_mascotas BOOLEAN DEFAULT FALSE,
    tiempo_disponible VARCHAR(50),
    experiencia VARCHAR(255),
    preferencia_tipo VARCHAR(20),
    preferencia_tamano VARCHAR(30),
    preferencia_edad VARCHAR(30),
    rol VARCHAR(30) DEFAULT 'adoptante'
);


-- ==========================================
-- TABLA: REFUGIOS
-- ==========================================

CREATE TABLE refugios (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(150) NOT NULL,
    ciudad VARCHAR(100) NOT NULL,
    direccion VARCHAR(200),
    telefono VARCHAR(30),
    email VARCHAR(100)
);


-- ==========================================
-- TABLA: MASCOTAS
-- ==========================================

CREATE TABLE mascotas (
    id INT AUTO_INCREMENT PRIMARY KEY,
    refugio_id INT,
    nombre VARCHAR(100) NOT NULL,
    tipo VARCHAR(20) NOT NULL,
    edad INT NOT NULL,
    sexo VARCHAR(20),
    tamano VARCHAR(30),
    raza VARCHAR(100),
    ciudad VARCHAR(100),
    descripcion VARCHAR(500),
    personalidad VARCHAR(500),
    nivel_energia VARCHAR(30),
    compatible_ninos BOOLEAN DEFAULT FALSE,
    compatible_mascotas BOOLEAN DEFAULT FALSE,
    vacunado BOOLEAN DEFAULT FALSE,
    desparasitado BOOLEAN DEFAULT FALSE,
    esterilizado BOOLEAN DEFAULT FALSE,
    estado VARCHAR(30) DEFAULT 'Disponible',

    FOREIGN KEY (refugio_id)
        REFERENCES refugios(id)
);


-- ==========================================
-- TABLA: FAVORITOS
-- ==========================================

CREATE TABLE favoritos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    usuario_id INT NOT NULL,
    mascota_id INT NOT NULL,

    FOREIGN KEY (usuario_id)
        REFERENCES usuarios(id),

    FOREIGN KEY (mascota_id)
        REFERENCES mascotas(id),

    UNIQUE (usuario_id, mascota_id)
);


-- ==========================================
-- TABLA: ADOPCIONES
-- ==========================================

CREATE TABLE adopciones (
    id INT AUTO_INCREMENT PRIMARY KEY,
    usuario_id INT NOT NULL,
    mascota_id INT NOT NULL,
    fecha_solicitud DATE NOT NULL,
    motivo VARCHAR(500),
    lugar_mascota VARCHAR(255),
    personas_casa INT,
    tiene_otras_mascotas BOOLEAN DEFAULT FALSE,
    experiencia VARCHAR(500),
    responsable VARCHAR(100),
    estado VARCHAR(30) DEFAULT 'En revisión',

    FOREIGN KEY (usuario_id)
        REFERENCES usuarios(id),

    FOREIGN KEY (mascota_id)
        REFERENCES mascotas(id)
);


-- ==========================================
-- TABLA: ENTREVISTAS
-- ==========================================

CREATE TABLE entrevistas (
    id INT AUTO_INCREMENT PRIMARY KEY,
    adopcion_id INT NOT NULL,
    fecha DATE NOT NULL,
    hora TIME NOT NULL,
    modalidad VARCHAR(30),
    observaciones VARCHAR(500),
    estado VARCHAR(30) DEFAULT 'Programada',

    FOREIGN KEY (adopcion_id)
        REFERENCES adopciones(id)
);


-- ==========================================
-- TABLA: HISTORIAL VETERINARIO
-- ==========================================

CREATE TABLE historial_veterinario (
    id INT AUTO_INCREMENT PRIMARY KEY,
    mascota_id INT NOT NULL,
    tipo VARCHAR(50),
    descripcion VARCHAR(500),
    fecha DATE,
    proxima_fecha DATE,

    FOREIGN KEY (mascota_id)
        REFERENCES mascotas(id)
);