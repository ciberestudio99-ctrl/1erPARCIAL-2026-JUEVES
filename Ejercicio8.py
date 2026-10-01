class Nodo:
    def __init__(self, dato, sig=None):
        self._elem = dato
        self._nxt = sig


class IteradorListaEnlazada:
    def __init__(self, nodo_inicial):
        self._actual = nodo_inicial

    def __iter__(self):
        return self

    def __next__(self):
        if self._actual is None:
            raise StopIteration
        dato = self._actual._elem
        self._actual = self._actual._nxt
        return dato


class ListaEnlazada:
    def __init__(self):
        self.header = Nodo(None)
        self._cantidad = 0

    def __len__(self):
        return self._cantidad

    def __iter__(self):
        return IteradorListaEnlazada(self.header._nxt)

    def esta_vacia(self):
        return self._cantidad == 0

    def agregar(self, dato):
        """Agrega un elemento al final de la lista."""
        actual = self.header
        while actual._nxt is not None:
            actual = actual._nxt
        actual._nxt = Nodo(dato)
        self._cantidad += 1

    append = agregar

    def buscar(self, criterio):
        """Busca por igualdad o usando una función criterio."""
        for dato in self:
            coincide = criterio(dato) if callable(criterio) else dato == criterio
            if coincide:
                return dato
        return None

    def remover(self, criterio):
        """Remueve el primer elemento coincidente y lo devuelve."""
        anterior = self.header
        actual = anterior._nxt

        while actual is not None:
            coincide = criterio(actual._elem) if callable(criterio) else actual._elem == criterio
            if coincide:
                anterior._nxt = actual._nxt
                self._cantidad -= 1
                return actual._elem
            anterior = actual
            actual = actual._nxt

        return None

    def a_lista(self):
        return list(self)
