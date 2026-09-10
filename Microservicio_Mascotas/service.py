from spyne import ServiceBase, rpc
from spyne import Integer, Unicode, Boolean

import repository


# MICROSERVICIO DE MASCOTAS

class PetService(ServiceBase):



    # 1. BUSCAR MASCOTAS DISPONIBLES POR CIUDAD


    @rpc(
        Unicode,
        _returns=Unicode
    )
    def search_available_by_city(ctx, city):

        try:

            pets = repository.search_available_by_city(city)

            if not pets:
                return (
                    f"No hay mascotas disponibles "
                    f"en la ciudad: {city}"
                )

            resultado = (
                f"MASCOTAS DISPONIBLES EN {city}\n\n"
            )

            for pet in pets:

                resultado += (
                    f"ID: {pet['id']}\n"
                    f"Nombre: {pet['nombre']}\n"
                    f"Tipo: {pet['tipo']}\n"
                    f"Edad: {pet['edad']} años\n"
                    f"Sexo: {pet['sexo']}\n"
                    f"Tamaño: {pet['tamano']}\n"
                    f"Raza: {pet['raza']}\n"
                    f"Ciudad: {pet['ciudad']}\n"
                    f"Descripción: {pet['descripcion']}\n"
                    f"Personalidad: {pet['personalidad']}\n"
                    f"Nivel de energía: {pet['nivel_energia']}\n"
                    f"Compatible con niños: "
                    f"{pet['compatible_ninos']}\n"
                    f"Compatible con mascotas: "
                    f"{pet['compatible_mascotas']}\n"
                    f"Vacunado: {pet['vacunado']}\n"
                    f"Desparasitado: "
                    f"{pet['desparasitado']}\n"
                    f"Esterilizado: "
                    f"{pet['esterilizado']}\n"
                    f"Estado: {pet['estado']}\n"
                    f"-----------------------------------\n"
                )

            return resultado

        except Exception as e:

            return f"Error al buscar mascotas: {str(e)}"



    # 2. FILTRAR POR TIPO Y EDAD


    @rpc(
        Unicode,
        Integer,
        Integer,
        _returns=Unicode
    )
    def filter_by_type_and_age(
        ctx,
        pet_type,
        min_age,
        max_age
    ):

        try:

            pets = repository.filter_by_type_and_age(
                pet_type,
                min_age,
                max_age
            )

            if not pets:
                return (
                    "No se encontraron mascotas "
                    "con esos criterios."
                )

            resultado = (
                "MASCOTAS FILTRADAS\n\n"
            )

            for pet in pets:

                resultado += (
                    f"ID: {pet['id']}\n"
                    f"Nombre: {pet['nombre']}\n"
                    f"Tipo: {pet['tipo']}\n"
                    f"Edad: {pet['edad']} años\n"
                    f"Sexo: {pet['sexo']}\n"
                    f"Tamaño: {pet['tamano']}\n"
                    f"Raza: {pet['raza']}\n"
                    f"Ciudad: {pet['ciudad']}\n"
                    f"Estado: {pet['estado']}\n"
                    f"-----------------------------------\n"
                )

            return resultado

        except Exception as e:

            return (
                f"Error al filtrar mascotas: {str(e)}"
            )



    # 3. BUSCAR MASCOTAS COMPATIBLES


    @rpc(
        Boolean,
        Boolean,
        Unicode,
        _returns=Unicode
    )
    def find_compatible_pets(
        ctx,
        has_children,
        has_other_pets,
        preferred_size
    ):

        try:

            pets = repository.find_compatible_pets(
                has_children,
                has_other_pets,
                preferred_size
            )

            if not pets:
                return (
                    "No se encontraron mascotas "
                    "compatibles con los criterios."
                )

            resultado = (
                "MASCOTAS COMPATIBLES\n\n"
            )

            for pet in pets:

                resultado += (
                    f"ID: {pet['id']}\n"
                    f"Nombre: {pet['nombre']}\n"
                    f"Tipo: {pet['tipo']}\n"
                    f"Edad: {pet['edad']} años\n"
                    f"Tamaño: {pet['tamano']}\n"
                    f"Raza: {pet['raza']}\n"
                    f"Ciudad: {pet['ciudad']}\n"
                    f"Compatible con niños: "
                    f"{pet['compatible_ninos']}\n"
                    f"Compatible con mascotas: "
                    f"{pet['compatible_mascotas']}\n"
                    f"Estado: {pet['estado']}\n"
                    f"-----------------------------------\n"
                )

            return resultado

        except Exception as e:

            return (
                f"Error al buscar mascotas compatibles: "
                f"{str(e)}"
            )



    # 4. RECOMENDAR MASCOTAS


    @rpc(
        Unicode,
        Unicode,
        Integer,
        Integer,
        Boolean,
        Boolean,
        _returns=Unicode
    )
    def recommend_pets(
        ctx,
        preferred_type,
        preferred_size,
        min_age,
        max_age,
        accepts_children,
        accepts_other_pets
    ):

        try:

            pets = repository.recommend_pets(
                preferred_type,
                preferred_size,
                min_age,
                max_age,
                accepts_children,
                accepts_other_pets
            )

            if not pets:
                return (
                    "No se encontraron mascotas "
                    "que coincidan con las preferencias."
                )

            resultado = (
                "RECOMENDACIONES DE MASCOTAS\n\n"
            )

            for pet in pets:

                resultado += (
                    f"ID: {pet['id']}\n"
                    f"Nombre: {pet['nombre']}\n"
                    f"Tipo: {pet['tipo']}\n"
                    f"Edad: {pet['edad']} años\n"
                    f"Tamaño: {pet['tamano']}\n"
                    f"Raza: {pet['raza']}\n"
                    f"Ciudad: {pet['ciudad']}\n"
                    f"Descripción: {pet['descripcion']}\n"
                    f"Personalidad: {pet['personalidad']}\n"
                    f"Nivel de energía: "
                    f"{pet['nivel_energia']}\n"
                    f"Compatible con niños: "
                    f"{pet['compatible_ninos']}\n"
                    f"Compatible con mascotas: "
                    f"{pet['compatible_mascotas']}\n"
                    f"Estado: {pet['estado']}\n"
                    f"-----------------------------------\n"
                )

            return resultado

        except Exception as e:

            return (
                f"Error al recomendar mascotas: "
                f"{str(e)}"
            )



    # 5. ESTADÍSTICAS


    @rpc(
        _returns=Unicode
    )
    def get_pet_statistics(ctx):

        try:

            statistics = repository.get_pet_statistics()

            resultado = (
                "ESTADÍSTICAS DE MASCOTAS\n\n"
                f"Total de mascotas: "
                f"{statistics['total']}\n"
                f"Mascotas disponibles: "
                f"{statistics['available']}\n"
                f"Mascotas adoptadas: "
                f"{statistics['adopted']}\n"
                f"Perros: "
                f"{statistics['dogs']}\n"
                f"Gatos: "
                f"{statistics['cats']}\n\n"
                f"MASCOTAS POR TIPO\n"
            )

            for item in statistics["by_type"]:

                resultado += (
                    f"{item['tipo']}: "
                    f"{item['cantidad']}\n"
                )

            resultado += (
                "\nMASCOTAS POR ESTADO\n"
            )

            for item in statistics["by_status"]:

                resultado += (
                    f"{item['estado']}: "
                    f"{item['cantidad']}\n"
                )

            return resultado

        except Exception as e:

            return (
                f"Error al obtener estadísticas: "
                f"{str(e)}"
            )
