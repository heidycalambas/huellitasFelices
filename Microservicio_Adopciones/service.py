from spyne import ServiceBase, rpc
from spyne import Integer, Unicode, Boolean

import repository


# MICROSERVICIO DE ADOPCIONES

class AdoptionService(ServiceBase):


    # 1. CREAR SOLICITUD DE ADOPCIÓN

    @rpc(
        Integer,
        Integer,
        Unicode,
        Unicode,
        Unicode,
        Integer,
        Boolean,
        Unicode,
        Unicode,
        _returns=Unicode
    )
    def create_adoption(
        ctx,
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

        try:

            adoption_id = repository.create_adoption(
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

            return (
                "Solicitud de adopción creada "
                "correctamente. "
                f"ID: {adoption_id}"
            )

        except Exception as e:

            return (
                "Error al crear la solicitud "
                f"de adopción: {str(e)}"
            )


    # 2. OBTENER TODAS LAS ADOPCIONES
    
    @rpc(
        _returns=Unicode
    )
    def get_all_adoptions(ctx):

        try:

            adoptions = repository.get_all_adoptions()

            if not adoptions:
                return (
                    "No existen solicitudes "
                    "de adopción."
                )

            resultado = (
                "SOLICITUDES DE ADOPCIÓN\n\n"
            )

            for adoption in adoptions:

                resultado += (
                    f"ID adopción: "
                    f"{adoption['id']}\n"
                    f"ID usuario: "
                    f"{adoption['usuario_id']}\n"
                    f"Usuario: "
                    f"{adoption['usuario_nombre']}\n"
                    f"ID mascota: "
                    f"{adoption['mascota_id']}\n"
                    f"Mascota: "
                    f"{adoption['mascota_nombre']}\n"
                    f"Tipo mascota: "
                    f"{adoption['mascota_tipo']}\n"
                    f"Fecha solicitud: "
                    f"{adoption['fecha_solicitud']}\n"
                    f"Motivo: "
                    f"{adoption['motivo']}\n"
                    f"Lugar: "
                    f"{adoption['lugar_mascota']}\n"
                    f"Personas en casa: "
                    f"{adoption['personas_casa']}\n"
                    f"Otras mascotas: "
                    f"{adoption['tiene_otras_mascotas']}\n"
                    f"Experiencia: "
                    f"{adoption['experiencia']}\n"
                    f"Responsable: "
                    f"{adoption['responsable']}\n"
                    f"Estado: "
                    f"{adoption['estado']}\n"
                    f"-----------------------------------\n"
                )

            return resultado

        except Exception as e:

            return (
                "Error al obtener las adopciones: "
                f"{str(e)}"
            )


    # 3. OBTENER ADOPCIÓN POR ID
    
    @rpc(
        Integer,
        _returns=Unicode
    )
    def get_adoption_by_id(
        ctx,
        adoption_id
    ):

        try:

            adoption = repository.get_adoption_by_id(
                adoption_id
            )

            if not adoption:

                return (
                    f"No existe una adopción "
                    f"con ID {adoption_id}."
                )

            resultado = (
                "DETALLE DE LA ADOPCIÓN\n\n"
                f"ID adopción: "
                f"{adoption['id']}\n"
                f"ID usuario: "
                f"{adoption['usuario_id']}\n"
                f"Usuario: "
                f"{adoption['usuario_nombre']}\n"
                f"Ciudad usuario: "
                f"{adoption['usuario_ciudad']}\n"
                f"ID mascota: "
                f"{adoption['mascota_id']}\n"
                f"Mascota: "
                f"{adoption['mascota_nombre']}\n"
                f"Tipo: "
                f"{adoption['mascota_tipo']}\n"
                f"Edad: "
                f"{adoption['mascota_edad']} años\n"
                f"Tamaño: "
                f"{adoption['mascota_tamano']}\n"
                f"Fecha solicitud: "
                f"{adoption['fecha_solicitud']}\n"
                f"Motivo: "
                f"{adoption['motivo']}\n"
                f"Lugar: "
                f"{adoption['lugar_mascota']}\n"
                f"Personas en casa: "
                f"{adoption['personas_casa']}\n"
                f"Otras mascotas: "
                f"{adoption['tiene_otras_mascotas']}\n"
                f"Experiencia: "
                f"{adoption['experiencia']}\n"
                f"Responsable: "
                f"{adoption['responsable']}\n"
                f"Estado: "
                f"{adoption['estado']}"
            )

            return resultado

        except Exception as e:

            return (
                "Error al consultar la adopción: "
                f"{str(e)}"
            )


    # 4. ACTUALIZAR ESTADO
    @rpc(
        Integer,
        Unicode,
        _returns=Unicode
    )
    def update_adoption_status(
        ctx,
        adoption_id,
        new_status
    ):

        try:

            updated = repository.update_adoption_status(
                adoption_id,
                new_status
            )

            if not updated:

                return (
                    f"No existe una adopción "
                    f"con ID {adoption_id}."
                )

            return (
                f"Estado de la adopción "
                f"{adoption_id} actualizado "
                f"correctamente a: {new_status}"
            )

        except Exception as e:

            return (
                "Error al actualizar el estado: "
                f"{str(e)}"
            )



    # 5. PROGRAMAR ENTREVISTA

    @rpc(
        Integer,
        Unicode,
        Unicode,
        Unicode,
        Unicode,
        _returns=Unicode
    )
    def schedule_interview(
        ctx,
        adoption_id,
        interview_date,
        interview_time,
        modality,
        observations
    ):

        try:

            scheduled = repository.schedule_interview(
                adoption_id,
                interview_date,
                interview_time,
                modality,
                observations
            )

            if not scheduled:

                return (
                    f"No existe una adopción "
                    f"con ID {adoption_id}."
                )

            return (
                f"Entrevista programada correctamente "
                f"para la adopción {adoption_id}."
            )

        except Exception as e:

            return (
                "Error al programar la entrevista: "
                f"{str(e)}"
            )
