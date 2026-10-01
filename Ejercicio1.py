from math import sqrt


def serie_potencias_homero(cantidad_terminos):
    """Devuelve la serie 1, sqrt(2), 2, 2*sqrt(2), ..."""
    if not isinstance(cantidad_terminos, int) or cantidad_terminos < 0:
        raise ValueError("La cantidad de términos debe ser un número natural.")

    return {
        posicion: sqrt(2) ** (posicion - 1)
        for posicion in range(1, cantidad_terminos + 1)
    }


if __name__ == "__main__":
    print(serie_potencias_homero(5))
