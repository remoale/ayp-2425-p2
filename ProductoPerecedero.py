from Producto import Producto
from datetime import date

class ProductoPerecedero(Producto):
    def __init__(self, nombre: str, precio: float, cantidad: int, fecha_expiracion):
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad
        self.fecha_expiracion = fecha_expiracion

    def expira_pronto(self):
        pass
