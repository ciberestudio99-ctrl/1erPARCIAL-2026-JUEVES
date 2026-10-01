from datetime import date, datetime


class ProductoKwikE:
    def __init__(self, descripcion, id_producto, fecha_vencimiento, precio, stock):
        self.descripcion = descripcion
        self.id_producto = id_producto
        self.fecha_vencimiento = self._convertir_fecha(fecha_vencimiento)
        self.precio = precio
        self.stock = stock
        self._validar_datos()

    @staticmethod
    def _convertir_fecha(valor):
        if isinstance(valor, datetime):
            return valor.date()
        if isinstance(valor, date):
            return valor
        raise TypeError("fecha_vencimiento debe ser date o datetime.")

    def _validar_datos(self):
        if not isinstance(self.descripcion, str) or not self.descripcion.strip():
            raise ValueError("La descripción no puede estar vacía.")
        if not isinstance(self.id_producto, int):
            raise TypeError("id_producto debe ser un entero.")
        if self.precio < 0 or self.stock < 0:
            raise ValueError("El precio y el stock no pueden ser negativos.")

    def actualizar_datos(self, descripcion=None, precio=None, stock=None):
        """Cambia uno o varios datos editables del producto."""
        if descripcion is not None:
            if not isinstance(descripcion, str) or not descripcion.strip():
                raise ValueError("La descripción no puede estar vacía.")
            self.descripcion = descripcion
        if precio is not None:
            if precio < 0:
                raise ValueError("El precio no puede ser negativo.")
            self.precio = precio
        if stock is not None:
            if not isinstance(stock, int) or stock < 0:
                raise ValueError("El stock debe ser un entero no negativo.")
            self.stock = stock

    def dias_para_vencer(self, fecha_actual=None):
        """Devuelve los días restantes; si expiró, deja el stock en cero."""
        if fecha_actual is None:
            fecha_actual = date.today()
        fecha_actual = self._convertir_fecha(fecha_actual)
        dias = (self.fecha_vencimiento - fecha_actual).days

        if dias < 0:
            self.stock = 0
            print(f"El producto {self.descripcion} está vencido.")

        return dias

    def __str__(self):
        return (
            f"Producto: {self.descripcion} | ID: {self.id_producto} | "
            f"Precio: ${self.precio:.2f} | Stock: {self.stock}"
        )

    def __eq__(self, otro):
        if not isinstance(otro, ProductoKwikE):
            return NotImplemented
        return (
            self.id_producto == otro.id_producto
            and self.descripcion == otro.descripcion
        )
