import bisect


def pesquisa_binaria_recursiva(a, esquerda, direita, item):
    if direita < esquerda:
        return -1
    meio = (esquerda + direita) // 2
    if a[meio] == item:
        return meio
    elif a[meio] > item:
        return pesquisa_binaria_recursiva(a, esquerda, meio - 1, item)
    else:
        return pesquisa_binaria_recursiva(a, meio + 1, direita, item)


def pesquisa_binaria(a, item):
    esquerda, direita = 0, len(a) - 1
    while esquerda <= direita:
        meio = (esquerda + direita) // 2
        if a[meio] == item:
            return meio
        elif a[meio] > item:
            direita = meio - 1
        else:
            esquerda = meio + 1
    return -1


def pesquisa_binaria_bisect(a, item):
    i = bisect.bisect_left(a, item)
    return i if i < len(a) and a[i] == item else -1

