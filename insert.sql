USE huellitas_felices;

INSERT INTO refugios
(nombre, ciudad, direccion, telefono, email)
VALUES
('Huellitas Popayan', 'Popayan', 'Carrera 6 # 10-25', '3001112233', 'huellitas.popayan@gmail.com'),
('Refugio Patitas Felices', 'Popayan', 'Calle 12 # 5-40', '3002223344', 'patitasfelices@gmail.com'),
('Fundacion Amigos Peludos', 'Cali', 'Carrera 20 # 15-30', '3003334455', 'amigospeludos@gmail.com');

INSERT INTO usuarios
(
    nombre,
    edad,
    ciudad,
    tipo_vivienda,
    tiene_patio,
    otras_mascotas,
    tiempo_disponible,
    experiencia,
    preferencia_tipo,
    preferencia_tamano,
    preferencia_edad,
    rol
)
VALUES
(
    'Carlos Perez',
    25,
    'Popayan',
    'Casa',
    1,
    0,
    'Alta',
    'Tiene experiencia cuidando perros',
    'Perro',
    'Mediano',
    'Joven',
    'adoptante'
),
(
    'Maria Gomez',
    30,
    'Popayan',
    'Apartamento',
    0,
    1,
    'Media',
    'Tiene experiencia con gatos',
    'Gato',
    'Pequeno',
    'Joven',
    'adoptante'
),
(
    'Juan Rodriguez',
    28,
    'Cali',
    'Casa',
    1,
    1,
    'Alta',
    'Experiencia con perros y gatos',
    'Perro',
    'Mediano',
    'Adulto',
    'adoptante'
),
(
    'Laura Sanchez',
    35,
    'Popayan',
    'Casa',
    1,
    0,
    'Media',
    'Primera vez teniendo mascota',
    'Perro',
    'Pequeno',
    'Joven',
    'adoptante'
);


INSERT INTO mascotas
(
    refugio_id,
    nombre,
    tipo,
    edad,
    sexo,
    tamano,
    raza,
    ciudad,
    descripcion,
    personalidad,
    nivel_energia,
    compatible_ninos,
    compatible_mascotas,
    vacunado,
    desparasitado,
    esterilizado,
    estado
)
VALUES
(
    1,
    'Luna',
    'Perro',
    2,
    'Hembra',
    'Mediano',
    'Labrador',
    'Popayan',
    'Perra joven, cariñosa y sociable.',
    'Amigable',
    'Alta',
    1,
    1,
    1,
    1,
    1,
    'Disponible'
),
(
    1,
    'Max',
    'Perro',
    5,
    'Macho',
    'Grande',
    'Pastor Aleman',
    'Popayan',
    'Perro tranquilo y protector.',
    'Leal',
    'Media',
    1,
    0,
    1,
    1,
    1,
    'Disponible'
),
(
    2,
    'Michi',
    'Gato',
    1,
    'Hembra',
    'Pequeno',
    'Criollo',
    'Popayan',
    'Gata pequena y juguetona.',
    'Juguetona',
    'Alta',
    1,
    1,
    1,
    1,
    0,
    'Disponible'
),
(
    2,
    'Simba',
    'Gato',
    4,
    'Macho',
    'Mediano',
    'Criollo',
    'Cali',
    'Gato tranquilo y cariñoso.',
    'Cariñoso',
    'Media',
    1,
    0,
    1,
    1,
    1,
    'Disponible'
),
(
    3,
    'Rocky',
    'Perro',
    8,
    'Macho',
    'Mediano',
    'Beagle',
    'Cali',
    'Perro adulto y tranquilo.',
    'Tranquilo',
    'Baja',
    1,
    1,
    1,
    1,
    1,
    'Adoptada'
),
(
    3,
    'Nala',
    'Perro',
    3,
    'Hembra',
    'Pequeno',
    'Criollo',
    'Bogota',
    'Perra pequena y activa.',
    'Juguetona',
    'Alta',
    0,
    1,
    1,
    1,
    0,
    'Disponible'
);

INSERT INTO adopciones
(
    usuario_id,
    mascota_id,
    fecha_solicitud,
    motivo,
    lugar_mascota,
    personas_casa,
    tiene_otras_mascotas,
    experiencia,
    responsable,
    estado
)
VALUES
(
    1,
    1,
    '2026-09-01',
    'Desea adoptar una mascota para compañía y cuenta con espacio suficiente.',
    'Casa con patio en Popayan',
    3,
    0,
    'Tiene experiencia cuidando perros.',
    'Carlos Perez',
    'En revisión'
),
(
    2,
    3,
    '2026-09-02',
    'Desea adoptar un gato joven para compañía.',
    'Apartamento en Popayan',
    2,
    1,
    'Tiene experiencia cuidando gatos.',
    'Maria Gomez',
    'Entrevista'
),
(
    3,
    4,
    '2026-09-03',
    'Desea adoptar una mascota para su familia.',
    'Casa con patio en Cali',
    4,
    1,
    'Tiene experiencia con perros y gatos.',
    'Juan Rodriguez',
    'Aprobada'
),
(
    4,
    6,
    '2026-09-04',
    'Busca una mascota pequeña para compañía.',
    'Casa con patio en Popayan',
    2,
    0,
    'No tiene experiencia previa.',
    'Laura Sanchez',
    'En revisión'
);


INSERT INTO entrevistas
(
    adopcion_id,
    fecha,
    hora,
    modalidad,
    observaciones,
    estado
)
VALUES
(
    1,
    '2026-09-10',
    '10:00:00',
    'Virtual',
    'Verificar condiciones de vivienda y disponibilidad de tiempo.',
    'Programada'
),
(
    2,
    '2026-09-11',
    '15:00:00',
    'Presencial',
    'Revisar compatibilidad con otras mascotas.',
    'Programada'
),
(
    3,
    '2026-09-08',
    '09:00:00',
    'Presencial',
    'Entrevista realizada satisfactoriamente.',
    'Realizada'
);