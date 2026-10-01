def total_interrupciones_recursivo(a, b):
    """Calcula a por b recursivamente mediante sumas repetidas."""
    if not isinstance(a, int) or not isinstance(b, int) or a < 0 or b < 0:
        raise ValueError("a y b deben ser números naturales.")

    if b == 0:
        return 0

    return a + total_interrupciones_recursivo(a, b - 1)


if __name__ == "__main__":
    print(total_interrupciones_recursivo(3, 4))
