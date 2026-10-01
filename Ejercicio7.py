from datetime import date, datetime

from Ejercicio5 import ProductoKwikE
from Ejercicio8 import ListaEnlazada


class KwikEMart:
    def __init__(self, nombres_pasillos=None):
        self.pasillos = {}
        for nombre in nombres_pasillos or []:
            self.agregar_pasillo(nombre)

    def agregar_pasillo(self, nombre):
        if not isinstance(nombre, str) or not nombre.strip():
            raise ValueError("El nombre del pasillo no puede estar vacío.")
        if nombre not in self.pasillos:
            self.pasillos[nombre] = ListaEnlazada()

    def agregar_producto(self, pasillo, producto):
        if not isinstance(producto, ProductoKwikE):
            raise TypeError("producto debe ser de tipo ProductoKwikE.")
        if pasillo not in self.pasillos:
            self.agregar_pasillo(pasillo)
        self.pasillos[pasillo].agregar(producto)

    def buscar_producto(self, id_producto):
        for productos in self.pasillos.values():
            encontrado = productos.buscar(
                lambda producto: producto.id_producto == id_producto
            )
            if encontrado is not None:
                return encontrado
        return None

    def remover_producto(self, id_producto):
        for productos in self.pasillos.values():
            eliminado = productos.remover(
                lambda producto: producto.id_producto == id_producto
            )
            if eliminado is not None:
                return eliminado
        return None

    def actualizar_stock(self, id_producto, nuevo_stock):
        producto = self.buscar_producto(id_producto)
        if producto is None:
            return False
        producto.actualizar_datos(stock=nuevo_stock)
        return True

    @staticmethod
    def _convertir_fecha(valor):
        if isinstance(valor, datetime):
            return valor.date()
        if isinstance(valor, date):
            return valor
        raise TypeError("fecha_actual debe ser date o datetime.")

    def retirar_productos_por_vencer(self, fecha_actual=None):
        """Retira productos vencidos o que vencen dentro de las próximas 24 h."""
        if fecha_actual is None:
            fecha_actual = date.today()
        fecha_actual = self._convertir_fecha(fecha_actual)
        retirados = 0

        for productos in self.pasillos.values():
            ids_a_retirar = [
                producto.id_producto
                for producto in productos
                if (producto.fecha_vencimiento - fecha_actual).days <= 1
            ]
            for id_producto in ids_a_retirar:
                productos.remover(
                    lambda producto, buscado=id_producto: producto.id_producto == buscado
                )
                retirados += 1

        return retirados


if __name__ == "__main__":
    tienda = KwikEMart(["Bebidas", "Snacks", "Conveniencia"])
