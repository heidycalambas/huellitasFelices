from spyne import (
    Application,
    rpc,
    ServiceBase,
    Integer,
    Unicode,
    Boolean,
    Date,
    Time,
    Iterable
)

from spyne.protocol.soap import Soap11

from models import Adoption

import repository


class AdoptionService(ServiceBase):

    # ==========================================
    # 1. CREAR SOLICITUD DE ADOPCIÓN
    # ==========================================

    @rpc(
        Integer,
        Integer,
        Date,
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

            repository.insert(
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

            return "Solicitud de adopción creada correctamente."

        except Exception as e:

            return f"Error al crear la solicitud: {str(e)}"


    # ==========================================
    # 2. OBTENER TODAS LAS ADOPCIONES
    # ==========================================

    @rpc(
        _returns=Iterable(Adoption)
    )
    def get_all_adoptions(ctx):

        return repository.find_all()


    # ==========================================
    # 3. OBTENER ADOPCIÓN POR ID
    # ==========================================

    @rpc(
        Integer,
        _returns=Adoption
    )
    def get_adoption_by_id(
        ctx,
        adoption_id
    ):

        return repository.find_by_id(adoption_id)


    # ==========================================
    # 4. ACTUALIZAR ESTADO DE ADOPCIÓN
    # ==========================================

    @rpc(
        Integer,
        Unicode,
        _returns=Unicode
    )
    def update_adoption_status(
        ctx,
        adoption_id,
        estado
    ):

        try:

            if repository.update_status(
                adoption_id,
                estado
            ):

                return (
                    f"Estado de la adopción ID "
                    f"{adoption_id} actualizado correctamente."
                )

            return (
                f"No se encontró la adopción "
                f"con ID {adoption_id}."
            )

        except Exception as e:

            return f"Error al actualizar: {str(e)}"


    # ==========================================
    # 5. PROGRAMAR ENTREVISTA
    # ==========================================

    @rpc(
        Integer,
        Date,
        Time,
        Unicode,
        Unicode,
        _returns=Unicode
    )
    def schedule_interview(
        ctx,
        adopcion_id,
        fecha,
        hora,
        modalidad,
        observaciones
    ):

        try:

            repository.insert_interview(
                adopcion_id,
                fecha,
                hora,
                modalidad,
                observaciones
            )

            return (
                "Entrevista programada "
                "correctamente."
            )

        except Exception as e:

            return (
                f"Error al programar entrevista: "
                f"{str(e)}"
            )


# ==========================================
# CONFIGURACIÓN SOAP
# ==========================================

application = Application(
    [AdoptionService],

    tns="huellitas_felices.adopciones",

    in_protocol=Soap11(
        validator="lxml"
    ),

    out_protocol=Soap11()
)