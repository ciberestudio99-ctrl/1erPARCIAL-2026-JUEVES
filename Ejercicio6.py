from datetime import date

from Ejercicio5 import ProductoKwikE


if __name__ == "__main__":
    producto_1 = ProductoKwikE("Donas glaseadas", 123, date(2026, 10, 2), 1.50, 50)
    producto_2 = ProductoKwikE("Donas glaseadas", 123, date(2026, 10, 3), 2.00, 20)

    print(producto_1)
    print(producto_1 == producto_2)
