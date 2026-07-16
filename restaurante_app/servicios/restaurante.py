from modelos.producto import Producto
from modelos.cliente import Cliente


class Restaurante:

    def __init__(self):
        self.productos: list[Producto] = []
        self.clientes: list[Cliente] = []

    def registrar_producto(self, producto: Producto) -> bool:
        for existente in self.productos:
            if existente.codigo == producto.codigo:
                return False

        self.productos.append(producto)
        return True

    def registrar_cliente(self, cliente: Cliente) -> bool:
        for existente in self.clientes:
            if existente.identificacion == cliente.identificacion:
                return False

        self.clientes.append(cliente)
        return True

    def listar_productos(self) -> None:
        if not self.productos:
            print("\nNo existen productos registrados.\n")
            return

        print("\n===== PRODUCTOS =====")

        for producto in self.productos:
            print(producto.mostrar_informacion())

    def listar_clientes(self) -> None:
        if not self.clientes:
            print("\nNo existen clientes registrados.\n")
            return

        print("\n===== CLIENTES =====")

        for cliente in self.clientes:
            print(cliente.mostrar_informacion())