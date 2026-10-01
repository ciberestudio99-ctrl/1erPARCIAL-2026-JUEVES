def total_donas_iterativo(a, b):
    """Calcula a por b mediante sumas repetidas."""
    if not isinstance(a, int) or not isinstance(b, int) or a < 0 or b < 0:
        raise ValueError("a y b deben ser números naturales.")

    total = 0
    for _ in range(b):
        total += a

    return total


if __name__ == "__main__":
    print(total_donas_iterativo(4, 5))
