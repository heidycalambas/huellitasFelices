from spyne import ComplexModel, Integer, Unicode, Boolean


class Pet(ComplexModel):

    id = Integer
    refugio_id = Integer

    name = Unicode
    type = Unicode
    age = Integer
    sex = Unicode
    size = Unicode
    breed = Unicode
    city = Unicode

    description = Unicode
    personality = Unicode
    energy_level = Unicode

    compatible_children = Boolean
    compatible_pets = Boolean

    vaccinated = Boolean
    dewormed = Boolean
    sterilized = Boolean

    status = Unicode