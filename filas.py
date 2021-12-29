class Nodo:
    def __init__(self, dado=0, proximo_nodo=None):
        self.dado = dado
        self.proximo = proximo_nodo

    def __repr__(self):
        return '%s -> %s' % (self.dado, self.proximo)


class Fila:
    def __init__(self):
        self.primeiro = None
        self.ultimo = None

    def __repr__(self):
        return "[" + str(self.primeiro) + "]"

    def insere(self, novo_dado):
        novo_nodo = Nodo(novo_dado)
        if self.primeiro == None:
            self.primeiro = novo_nodo
            self.ultimo = novo_nodo
        else:
            self.ultimo.proximo = novo_nodo
            self.ultimo = novo_nodo

    def remove(self):
        assert self.primeiro is not None
        self.primeiro = self.primeiro.proximo
        if self.primeiro is None:
            self.ultimo = None


# Testes
fila = Fila()
print("Fila vazia: ", fila)

for i in range(5):
    fila.insere(i)
    print("Insere o valor {0} final da fila: {1}".format(i, fila))

while fila.primeiro is not None:
    fila.remove()
    print("Removendo elemento que está no começo da fila: ", fila)
