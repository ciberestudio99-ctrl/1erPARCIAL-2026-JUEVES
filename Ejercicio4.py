def ordenar_eventos(eventos, descendente=False):
    """Ordena los eventos de A a Z o de Z a A."""
    if not isinstance(eventos, list):
        raise TypeError("eventos debe ser una lista.")

    return sorted(eventos, reverse=bool(descendente))


if __name__ == "__main__":
    agenda = ["Kermés", "Concurso de Comida", "Reunión del Concejo Municipal"]
    print(ordenar_eventos(agenda))
    print(ordenar_eventos(agenda, True))
