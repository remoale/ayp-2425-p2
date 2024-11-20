from Producto import Producto
from typing import List

class Inventario:
    def __init__(self):
        self.productos: List[Producto] = []


    def agregar(self):
        nombre = input('Nombre del producto: ').strip()
        try:
            precio = float(input('Precio del producto: '))
        except:
            print('El monto indicado no es un precio válido.')
            return
        try:
            cantidad = int(input('Cantidad del producto: '))
            if cantidad < 1:
                print('La cantidad indicada debe ser un número entero positivo')
                raise ValueError
        except:
            print('La cantidad indicada no es válida.')
            return
        producto = Producto(nombre, precio, cantidad)
        self.productos.append(producto)
        print(f'¡Producto {nombre} agregado con éxito!')
        return producto


    def eliminar(self, nombre: str):
        try:
            cantidad = int(input('Introduce la cantidad a eliminar: '))
        except:
            print('La cantidad indicada es inválida.')
            return
        producto = self.buscar(nombre)
        if producto:
            for producto in self.productos:
                if producto.nombre == nombre:
                    if cantidad > producto.cantidad:
                        print('La cantidad indicada es superior a la cantidad disponible.')
                        return
                    producto.cantidad -= cantidad
                    print(f'Se eliminaron {cantidad} {nombre} del inventario.')
                    if producto.cantidad == 0:
                        self.productos.remove(producto)
                        print(f'Producto {nombre} eliminado del inventario.')
        return producto
    

    def buscar(self, nombre: str):
        if nombre not in self.productos:
            print('Lo sentimos. Este producto no se encuentra en el inventario.')
            return
        for producto in self.productos:
            if producto.nombre == nombre:
                return producto


    def listar(self):
        for producto in self.productos:
            print(f'Producto: {producto.nombre}')
            print(f'Precio: {producto.precio}')
            print(f'Cantidad: {producto.cantidad}')
        
        print('1. Ordenar por nombre', '2. Ordenar por precio', '3. Ordenar por cantidad', sep='\n')
        try:
            option = int(input('Seleccione una opción'))
            if option not in [1, 2, 3]:
                raise ValueError
        except:
            print('Opción incorrecta')
            return
        
        if option == 1:
            nombres = [producto.nombre for nombre in self.productos]
            for nombre in nombres:
                for producto in self.products:
                    if producto.nombre in nombres:
                        print(f'Producto: {producto.nombre}')
        if option == 2:
            precios = [producto.precio for precio in self.productos]
            for precio in precios:
                    for producto in self.products:
                        if producto.precio in precios:
                            print(f'Producto: {producto.precio}')
        if option == 3:
            cantidades = [producto.cantidad for cantidad in self.productos]
            for cantidad in cantidades:
                    for producto in self.products:
                        if producto.cantidad in cantidades:
                            print(f'Producto: {producto.cantidad}')
    

    def valor_total(self):
        total = 0
        def valor(precio, cantidad):
            return valor(precio * cantidad)
        for producto in self.productos:
             return valor(producto.precio, producto.cantidad)

    def menu(self):
        print('¡Bienvenido al inventario!\n')
        option = None
        while option not in [0, 1, 2, 3, 4]:
            print('1. Agregar un producto', '2. Eliminar un producto',
                  '3. Buscar un producto', '4. Listar todos los productos disponibles',
                  '0. Salir', '', sep='\n')
            try:
                option = int(input('Selecciona una opción: '))
                if option == 0:
                    return
                elif option == 1:
                    self.agregar()
                elif option == 2:
                    self.eliminar()
                elif option == 3:
                    nombre = input('Por favor indica el nombre del producto: ').strip()
                    self.buscar(nombre)
                elif option == 4:
                    self.listar()
            except:
                continue
