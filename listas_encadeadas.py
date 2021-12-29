class NodoLista:
    def __init__(self, dado=0, proximo_nodo=None):
        self.dado = dado
        self.proximo = proximo_nodo

    def __repr__(self):
        return '%s -> %s' % (self.dado, self.proximo)


class ListaEncadeada:
    def __init__(self):
        self.cabeca = None

    def __repr__(self):
        return "[" + str(self.cabeca) + "]"


def insere_no_inicio(lista, novo_dado):
    novo_nodo = NodoLista(novo_dado)
    novo_nodo.proximo = lista.cabeca
    lista.cabeca = novo_nodo


def insere_depois(lista, nodo_anterior, novo_dado):
    assert nodo_anterior
    novo_nodo = NodoLista(novo_dado)
    novo_nodo.proximo = nodo_anterior.proximo
    nodo_anterior.proximo = novo_nodo


def busca(lista, valor):
    corrente = lista.cabeca
    while corrente and corrente.dado != valor:
        corrente = corrente.proximo
    return corrente


def remove(self, valor):
    assert self.cabeca
    if self.cabeca.dado == valor:
        self.cabeca = self.cabeca.proximo
    else:
        anterior = None
        corrente = self.cabeca
        while corrente and corrente.dado != valor:
            anterior = corrente
            corrente = corrente.proximo
        if corrente:
            anterior.proximo = corrente.proximo
        else:
            anterior.proximo = None
