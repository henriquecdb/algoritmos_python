def pesquisa_linear(arranjo, elemento_desejado):
    for elemento in arranjo:
        if elemento == elemento_desejado:
            print("Elemento {} está presente no arranjo.".format(elemento_desejado))
            return
    print("Elemento {} não está presente no arranjo.".format(elemento_desejado))


def pesquisa_linear_in(arranjo, item):
    return item in arranjo


def pesquisa_linear_index(arranjo, item):
    try:
        return arranjo.index(item)
    except ValueError:
        return -1
