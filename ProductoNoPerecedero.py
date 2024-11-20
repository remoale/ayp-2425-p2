from Producto import Producto

class ProductoNoPerecedero(Producto):
    def __init__(self, nombre, precio, cantidad, material):
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad
        self.material = material

    def tipo_material(self):
        pass
