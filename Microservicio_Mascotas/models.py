from spyne import (
    ComplexModel,
    Integer,
    Unicode,
    Boolean,
    Date,
    Time
)


class Adoption(ComplexModel):

    id = Integer
    usuario_id = Integer
    mascota_id = Integer
    fecha_solicitud = Date

    motivo = Unicode
    lugar_mascota = Unicode

    personas_casa = Integer
    tiene_otras_mascotas = Boolean

    experiencia = Unicode
    responsable = Unicode

    estado = Unicode


class Interview(ComplexModel):

    id = Integer
    adopcion_id = Integer

    fecha = Date
    hora = Time

    modalidad = Unicode
    observaciones = Unicode
    estado = Unicode