from spyne import ComplexModel, Integer, Unicode, Float

class Product(ComplexModel):
    id = Integer
    name = Unicode
    price = Float
    stock = Integer
