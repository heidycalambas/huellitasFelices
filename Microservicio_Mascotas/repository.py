import pymysql


# CONFIGURACIÓN DE BASE DE DATOS

DB_HOST = "localhost"
DB_USER = "root"
DB_PASSWORD = "1003418409"
DB_NAME = "huellitas_felices"


# CONEXIÓN A MYSQL

def get_connection():
    return pymysql.connect(
        host=DB_HOST,
        user=DB_USER,
        password=DB_PASSWORD,
        database=DB_NAME,
        cursorclass=pymysql.cursors.DictCursor
    )


# 1. BUSCAR MASCOTAS DISPONIBLES POR CIUDAD

def search_available_by_city(city):

    connection = get_connection()

    try:
        with connection.cursor() as cursor:

            sql = """
                SELECT
                    id,
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
                FROM mascotas
                WHERE ciudad = %s
                  AND estado = 'Disponible'
                ORDER BY nombre ASC
            """

            cursor.execute(sql, (city,))

            return cursor.fetchall()

    finally:
        connection.close()


# 2. FILTRAR POR TIPO Y EDAD

def filter_by_type_and_age(pet_type, min_age, max_age):

    connection = get_connection()

    try:
        with connection.cursor() as cursor:

            sql = """
                SELECT
                    id,
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
                FROM mascotas
                WHERE tipo = %s
                  AND edad BETWEEN %s AND %s
                  AND estado = 'Disponible'
                ORDER BY edad ASC
            """

            cursor.execute(
                sql,
                (
                    pet_type,
                    min_age,
                    max_age
                )
            )

            return cursor.fetchall()

    finally:
        connection.close()


# 3. BUSCAR MASCOTAS COMPATIBLES

def find_compatible_pets(
    has_children,
    has_other_pets,
    preferred_size
):

    connection = get_connection()

    try:
        with connection.cursor() as cursor:

            sql = """
                SELECT
                    id,
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
                FROM mascotas
                WHERE estado = 'Disponible'
                  AND tamano = %s
                  AND (
                        %s = 0
                        OR compatible_ninos = 1
                  )
                  AND (
                        %s = 0
                        OR compatible_mascotas = 1
                  )
                ORDER BY nombre ASC
            """

            cursor.execute(
                sql,
                (
                    preferred_size,
                    int(has_children),
                    int(has_other_pets)
                )
            )

            return cursor.fetchall()

    finally:
        connection.close()


# 4. RECOMENDAR MASCOTAS

def recommend_pets(
    preferred_type,
    preferred_size,
    min_age,
    max_age,
    accepts_children,
    accepts_other_pets
):

    connection = get_connection()

    try:
        with connection.cursor() as cursor:

            sql = """
                SELECT
                    id,
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
                FROM mascotas
                WHERE estado = 'Disponible'
                  AND (
                        %s = ''
                        OR tipo = %s
                  )
                  AND (
                        %s = ''
                        OR tamano = %s
                  )
                  AND edad BETWEEN %s AND %s
                  AND (
                        %s = 0
                        OR compatible_ninos = 1
                  )
                  AND (
                        %s = 0
                        OR compatible_mascotas = 1
                  )
                ORDER BY edad ASC, nombre ASC
            """

            cursor.execute(
                sql,
                (
                    preferred_type,
                    preferred_type,
                    preferred_size,
                    preferred_size,
                    min_age,
                    max_age,
                    int(accepts_children),
                    int(accepts_other_pets)
                )
            )

            return cursor.fetchall()

    finally:
        connection.close()


# 5. ESTADÍSTICAS DE MASCOTAS

def get_pet_statistics():

    connection = get_connection()

    try:
        with connection.cursor() as cursor:

            # Total
            cursor.execute("""
                SELECT COUNT(*) AS total
                FROM mascotas
            """)

            total = cursor.fetchone()["total"]

            # Disponibles
            cursor.execute("""
                SELECT COUNT(*) AS total
                FROM mascotas
                WHERE estado = 'Disponible'
            """)

            available = cursor.fetchone()["total"]

            # Adoptadas
            cursor.execute("""
                SELECT COUNT(*) AS total
                FROM mascotas
                WHERE estado = 'Adoptada'
            """)

            adopted = cursor.fetchone()["total"]

            # Perros
            cursor.execute("""
                SELECT COUNT(*) AS total
                FROM mascotas
                WHERE tipo = 'Perro'
            """)

            dogs = cursor.fetchone()["total"]

            # Gatos
            cursor.execute("""
                SELECT COUNT(*) AS total
                FROM mascotas
                WHERE tipo = 'Gato'
            """)

            cats = cursor.fetchone()["total"]

            # Por tipo
            cursor.execute("""
                SELECT
                    tipo,
                    COUNT(*) AS cantidad
                FROM mascotas
                GROUP BY tipo
                ORDER BY tipo
            """)

            by_type = cursor.fetchall()

            # Por estado
            cursor.execute("""
                SELECT
                    estado,
                    COUNT(*) AS cantidad
                FROM mascotas
                GROUP BY estado
                ORDER BY estado
            """)

            by_status = cursor.fetchall()

            return {
                "total": total,
                "available": available,
                "adopted": adopted,
                "dogs": dogs,
                "cats": cats,
                "by_type": by_type,
                "by_status": by_status
            }

    finally:
        connection.close()
