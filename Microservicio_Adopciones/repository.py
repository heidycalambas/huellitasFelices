import pymysql  # Permite trabajar con la base de datos MySQL


# CONFIGURACIÓN DE BASE DE DATOS

DB_HOST = "localhost"
DB_USER = "root"
DB_PASSWORD = "1003418409"
DB_NAME = "huellitas_felices"



def get_connection():

    # Crea y devuelve la conexión con MySQL
    return pymysql.connect(
        host=DB_HOST,
        user=DB_USER,
        password=DB_PASSWORD,
        database=DB_NAME,
        cursorclass=pymysql.cursors.DictCursor
    )


# 1. CREAR SOLICITUD DE ADOPCIÓN

def create_adoption(
    usuario_id,
    mascota_id,
    fecha_solicitud,
    motivo,
    lugar_mascota,
    personas_casa,
    tiene_otras_mascotas,
    experiencia,
    responsable
):

    connection = get_connection()  

    try:

        with connection.cursor() as cursor:

            # Inserta la nueva solicitud de adopción
            sql = """
                INSERT INTO adopciones (
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
                VALUES (
                    %s,
                    %s,
                    %s,
                    %s,
                    %s,
                    %s,
                    %s,
                    %s,
                    %s,
                    'En revisión'
                )
            """

            cursor.execute(
                sql,
                (
                    usuario_id,
                    mascota_id,
                    fecha_solicitud,
                    motivo,
                    lugar_mascota,
                    personas_casa,
                    tiene_otras_mascotas,
                    experiencia,
                    responsable
                )
            )

            adoption_id = cursor.lastrowid  

            connection.commit()  # Guarda la solicitud en la base de datos

            return adoption_id  

    except Exception:

        connection.rollback()  # Deshace los cambios si ocurre un error
        raise

    finally:

        connection.close() 


# 2. OBTENER TODAS LAS ADOPCIONES

def get_all_adoptions():

    connection = get_connection() 

    try:

        with connection.cursor() as cursor:

            # Consulta todas las solicitudes y sus datos relacionados
            sql = """
                SELECT
                    a.id,
                    a.usuario_id,
                    u.nombre AS usuario_nombre,
                    a.mascota_id,
                    m.nombre AS mascota_nombre,
                    m.tipo AS mascota_tipo,
                    a.fecha_solicitud,
                    a.motivo,
                    a.lugar_mascota,
                    a.personas_casa,
                    a.tiene_otras_mascotas,
                    a.experiencia,
                    a.responsable,
                    a.estado
                FROM adopciones a
                INNER JOIN usuarios u
                    ON a.usuario_id = u.id
                INNER JOIN mascotas m
                    ON a.mascota_id = m.id
                ORDER BY a.id DESC
            """

            cursor.execute(sql)  

            return cursor.fetchall()  # Devuelve todas las adopciones encontradas

    finally:

        connection.close()  


# 3. OBTENER ADOPCIÓN POR ID

def get_adoption_by_id(adoption_id):

    connection = get_connection()  

    try:

        with connection.cursor() as cursor:

            # Busca una solicitud específica por su ID
            sql = """
                SELECT
                    a.id,
                    a.usuario_id,
                    u.nombre AS usuario_nombre,
                    u.ciudad AS usuario_ciudad,
                    a.mascota_id,
                    m.nombre AS mascota_nombre,
                    m.tipo AS mascota_tipo,
                    m.edad AS mascota_edad,
                    m.tamano AS mascota_tamano,
                    a.fecha_solicitud,
                    a.motivo,
                    a.lugar_mascota,
                    a.personas_casa,
                    a.tiene_otras_mascotas,
                    a.experiencia,
                    a.responsable,
                    a.estado
                FROM adopciones a
                INNER JOIN usuarios u
                    ON a.usuario_id = u.id
                INNER JOIN mascotas m
                    ON a.mascota_id = m.id
                WHERE a.id = %s
            """

            cursor.execute(
                sql,
                (adoption_id,)
            )

            return cursor.fetchone()  # Devuelve la solicitud encontrada

    finally:

        connection.close()  


# 4. ACTUALIZAR ESTADO DE ADOPCIÓN

def update_adoption_status(
    adoption_id,
    new_status
):

    connection = get_connection()  

    try:

        with connection.cursor() as cursor:

            # Primero verifica que la solicitud exista
            cursor.execute(
                """
                SELECT id
                FROM adopciones
                WHERE id = %s
                """,
                (adoption_id,)
            )

            adoption = cursor.fetchone()

            if not adoption:
                return False  # Indica que no se encontró la solicitud

            # Cambia el estado de la solicitud
            sql = """
                UPDATE adopciones
                SET estado = %s
                WHERE id = %s
            """

            cursor.execute(
                sql,
                (
                    new_status,
                    adoption_id
                )
            )

            connection.commit()  # Guarda el nuevo estado

            return True  # Indica que la actualización fue exitosa

    except Exception:

        connection.rollback()  # Deshace el cambio si ocurre un error
        raise

    finally:

        connection.close()  


# 5. PROGRAMAR ENTREVISTA

def schedule_interview(
    adoption_id,
    interview_date,
    interview_time,
    modality,
    observations
):

    connection = get_connection() 

    try:

        with connection.cursor() as cursor:

            # Verifica que exista la solicitud de adopción
            cursor.execute(
                """
                SELECT id
                FROM adopciones
                WHERE id = %s
                """,
                (adoption_id,)
            )

            adoption = cursor.fetchone()

            if not adoption:
                return False  # No permite programar si no existe la adopción

            # Guarda los datos de la entrevista
            sql = """
                INSERT INTO entrevistas (
                    adopcion_id,
                    fecha,
                    hora,
                    modalidad,
                    observaciones,
                    estado
                )
                VALUES (
                    %s,
                    %s,
                    %s,
                    %s,
                    %s,
                    'Programada'
                )
            """

            cursor.execute(
                sql,
                (
                    adoption_id,
                    interview_date,
                    interview_time,
                    modality,
                    observations
                )
            )

            connection.commit()  # Guarda la entrevista

            return True  

    except Exception:

        connection.rollback()  
        raise

    finally:

        connection.close() 
