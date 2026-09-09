from database import get_cursor

from models import Adoption, Interview


def _row_to_adoption(row: dict) -> Adoption:

    return Adoption(
        id=row["id"],
        usuario_id=row["usuario_id"],
        mascota_id=row["mascota_id"],
        fecha_solicitud=row["fecha_solicitud"],
        motivo=row["motivo"],
        lugar_mascota=row["lugar_mascota"],
        personas_casa=row["personas_casa"],
        tiene_otras_mascotas=row["tiene_otras_mascotas"],
        experiencia=row["experiencia"],
        responsable=row["responsable"],
        estado=row["estado"],
    )


def _row_to_interview(row: dict) -> Interview:

    return Interview(
        id=row["id"],
        adopcion_id=row["adopcion_id"],
        fecha=row["fecha"],
        hora=row["hora"],
        modalidad=row["modalidad"],
        observaciones=row["observaciones"],
        estado=row["estado"],
    )


# ==========================================
# 1. BUSCAR TODAS LAS ADOPCIONES
# ==========================================

def find_all() -> list[Adoption]:

    with get_cursor() as cursor:

        cursor.execute("""
            SELECT
                id,
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
            FROM adopciones
            ORDER BY id DESC
        """)

        return [
            _row_to_adoption(row)
            for row in cursor.fetchall()
        ]


# ==========================================
# 2. BUSCAR ADOPCIÓN POR ID
# ==========================================

def find_by_id(adoption_id: int) -> Adoption | None:

    with get_cursor() as cursor:

        cursor.execute("""
            SELECT
                id,
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
            FROM adopciones
            WHERE id = %s
        """, (adoption_id,))

        row = cursor.fetchone()

        return _row_to_adoption(row) if row else None


# ==========================================
# 3. INSERTAR ADOPCIÓN
# ==========================================

def insert(
    usuario_id: int,
    mascota_id: int,
    fecha_solicitud,
    motivo: str,
    lugar_mascota: str,
    personas_casa: int,
    tiene_otras_mascotas: bool,
    experiencia: str,
    responsable: str
) -> None:

    with get_cursor(commit=True) as cursor:

        cursor.execute("""
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
                %s, %s, %s, %s, %s,
                %s, %s, %s, %s,
                'En revisión'
            )
        """, (
            usuario_id,
            mascota_id,
            fecha_solicitud,
            motivo,
            lugar_mascota,
            personas_casa,
            tiene_otras_mascotas,
            experiencia,
            responsable
        ))


# ==========================================
# 4. ACTUALIZAR ESTADO
# ==========================================

def update_status(
    adoption_id: int,
    estado: str
) -> bool:

    with get_cursor(commit=True) as cursor:

        cursor.execute("""
            UPDATE adopciones
            SET estado = %s
            WHERE id = %s
        """, (
            estado,
            adoption_id
        ))

        return cursor.rowcount > 0


# ==========================================
# 5. PROGRAMAR ENTREVISTA
# ==========================================

def insert_interview(
    adopcion_id: int,
    fecha,
    hora,
    modalidad: str,
    observaciones: str
) -> None:

    with get_cursor(commit=True) as cursor:

        cursor.execute("""
            INSERT INTO entrevistas (
                adopcion_id,
                fecha,
                hora,
                modalidad,
                observaciones,
                estado
            )
            VALUES (
                %s, %s, %s, %s, %s, 'Programada'
            )
        """, (
            adopcion_id,
            fecha,
            hora,
            modalidad,
            observaciones
        ))