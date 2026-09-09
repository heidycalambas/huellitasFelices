from database import get_cursor
from models import Pet


def _row_to_pet(row: dict) -> Pet:

    return Pet(
        id=row["id"],
        refugio_id=row["refugio_id"],
        name=row["nombre"],
        type=row["tipo"],
        age=row["edad"],
        sex=row["sexo"],
        size=row["tamano"],
        breed=row["raza"],
        city=row["ciudad"],
        description=row["descripcion"],
        personality=row["personalidad"],
        energy_level=row["nivel_energia"],
        compatible_children=row["compatible_ninos"],
        compatible_pets=row["compatible_mascotas"],
        vaccinated=row["vacunado"],
        dewormed=row["desparasitado"],
        sterilized=row["esterilizado"],
        status=row["estado"]
    )


def find_all() -> list[Pet]:

    with get_cursor() as cursor:

        cursor.execute("""
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
        """)

        return [_row_to_pet(row) for row in cursor.fetchall()]


def find_by_id(pet_id: int) -> Pet | None:

    with get_cursor() as cursor:

        cursor.execute("""
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
            WHERE id = %s
        """, (pet_id,))

        row = cursor.fetchone()

        return _row_to_pet(row) if row else None


def insert(
    refugio_id,
    name,
    pet_type,
    age,
    sex,
    size,
    breed,
    city,
    description,
    personality,
    energy_level,
    compatible_children,
    compatible_pets,
    vaccinated,
    dewormed,
    sterilized,
    status
):

    with get_cursor(commit=True) as cursor:

        cursor.execute("""
            INSERT INTO mascotas (
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
            VALUES (
                %s, %s, %s, %s, %s, %s, %s,
                %s, %s, %s, %s, %s, %s, %s,
                %s, %s, %s
            )
        """, (
            refugio_id,
            name,
            pet_type,
            age,
            sex,
            size,
            breed,
            city,
            description,
            personality,
            energy_level,
            compatible_children,
            compatible_pets,
            vaccinated,
            dewormed,
            sterilized,
            status
        ))


def update(
    pet_id,
    refugio_id,
    name,
    pet_type,
    age,
    sex,
    size,
    breed,
    city,
    description,
    personality,
    energy_level,
    compatible_children,
    compatible_pets,
    vaccinated,
    dewormed,
    sterilized,
    status
):

    with get_cursor(commit=True) as cursor:

        cursor.execute("""
            UPDATE mascotas
            SET
                refugio_id = %s,
                nombre = %s,
                tipo = %s,
                edad = %s,
                sexo = %s,
                tamano = %s,
                raza = %s,
                ciudad = %s,
                descripcion = %s,
                personalidad = %s,
                nivel_energia = %s,
                compatible_ninos = %s,
                compatible_mascotas = %s,
                vacunado = %s,
                desparasitado = %s,
                esterilizado = %s,
                estado = %s
            WHERE id = %s
        """, (
            refugio_id,
            name,
            pet_type,
            age,
            sex,
            size,
            breed,
            city,
            description,
            personality,
            energy_level,
            compatible_children,
            compatible_pets,
            vaccinated,
            dewormed,
            sterilized,
            status,
            pet_id
        ))

        return cursor.rowcount > 0


def delete(pet_id: int) -> bool:

    with get_cursor(commit=True) as cursor:

        cursor.execute(
            "DELETE FROM mascotas WHERE id = %s",
            (pet_id,)
        )

        return cursor.rowcount > 0