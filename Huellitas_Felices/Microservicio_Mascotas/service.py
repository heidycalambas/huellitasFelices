from spyne import Application, rpc, ServiceBase, Integer, Unicode, Boolean, Iterable

from spyne.protocol.soap import Soap11

from models import Pet
import repository


class PetService(ServiceBase):

    # ==========================================
    # 1. CONSULTAR TODAS LAS MASCOTAS
    # ==========================================

    @rpc(_returns=Iterable(Pet))
    def get_all_pets(ctx):

        return repository.find_all()


    # ==========================================
    # 2. CONSULTAR MASCOTA POR ID
    # ==========================================

    @rpc(Integer, _returns=Pet)
    def get_pet_by_id(ctx, pet_id):

        return repository.find_by_id(pet_id)

    # ==========================================
    # 3. REGISTRAR MASCOTA
    # ==========================================

    @rpc(
        Integer,       # refugio_id
        Unicode,       # name
        Unicode,       # pet_type
        Integer,       # age
        Unicode,       # sex
        Unicode,       # size
        Unicode,       # breed
        Unicode,       # city
        Unicode,       # description
        Unicode,       # personality
        Unicode,       # energy_level
        Boolean,       # compatible_children
        Boolean,       # compatible_pets
        Boolean,       # vaccinated
        Boolean,       # dewormed
        Boolean,       # sterilized
        _returns=Unicode
    )
    def add_pet(
        ctx,
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
        sterilized
    ):
        try:

            repository.insert(
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
                "Disponible"
            )

            return f"Mascota '{name}' registrada correctamente."

        except Exception as e:

            return f"Error al registrar mascota: {str(e)}"


    # ==========================================
    # 4. ACTUALIZAR MASCOTA
    # ==========================================

    @rpc(
        Integer,       # id
        Integer,       # refugio_id
        Unicode,       # name
        Unicode,       # pet_type
        Integer,       # age
        Unicode,       # sex
        Unicode,       # size
        Unicode,       # breed
        Unicode,       # city
        Unicode,       # description
        Unicode,       # personality
        Unicode,       # energy_level
        Boolean,       # compatible_children
        Boolean,       # compatible_pets
        Boolean,       # vaccinated
        Boolean,       # dewormed
        Boolean,       # sterilized
        Unicode,       # estado
        _returns=Unicode
    )
    def update_pet(
        ctx,
        id,
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
        estado
    ):
        try:

            repository.update(
                id,
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
                estado
            )

            return f"Mascota '{name}' actualizada correctamente."

        except Exception as e:

            return f"Error al actualizar mascota: {str(e)}"

    # ==========================================
    # 5. ELIMINAR MASCOTA
    # ==========================================

    @rpc(Integer, _returns=Unicode)
    def delete_pet(ctx, pet_id):

        try:

            if repository.delete(pet_id):

                return f"Mascota ID {pet_id} eliminada exitosamente."

            return f"No existe la mascota con ID {pet_id}."

        except Exception as e:

            return f"Error al eliminar: {str(e)}"


# ==========================================
# CONFIGURACIÓN SOAP
# ==========================================

application = Application(
    [PetService],
    tns="huellitas_felices.mascotas",
    in_protocol=Soap11(validator="lxml"),
    out_protocol=Soap11(),
)