class NodoArvore:
    def __init__(self,  chave=None, esquerda=None, direita=None):
        self.chave = chave
        self.esquerda = esquerda
        self.direita = direita

    def __repr__(self):
        return '%s <- %s -> %s' % (self.esquerda and self.esquerda.chave,
                                   self.chave,
                                   self.direita and self.direita.chave)


def em_ordem(raiz):
    if not raiz:
        return
    em_ordem(raiz.esquerda)
    print(raiz.chave),
    em_ordem(raiz.direita)


def insere(raiz, nodo):
    if raiz is None:
        raiz = nodo
    elif raiz.chave < nodo.chave:
        if raiz.direita is None:
            raiz.direita = nodo
        else:
            insere(raiz.direita, nodo)
    else:
        if raiz.esquerda is None:
            raiz.esquerda = nodo
        else:
            insere(raiz.esquerda, nodo)


def busca(raiz, chave):
    if raiz is None:
        return None
    elif raiz.chave == chave:
        return raiz
    elif raiz.chave < chave:
        return busca(raiz.direita, chave)

    return busca(raiz.esquerda, chave)


def minimo(raiz):
    nodo = raiz
    while nodo.esquerda is not None:
        nodo = nodo.esquerda
    return nodo.chave


def maximo(raiz):
    nodo = raiz
    while nodo.direita is not None:
        nodo = nodo.direita
    return nodo.chave


def identicas(a, b):
    if a is None and b is None:
        return True

    if a is not None and b is not None:
        return((a.chave == b.chave) and
               identicas(a.esquerda, b.esquerda) and
               identicas(a.direita, b.direita))

    return False


def altura(raiz):
    if raiz is None:
        return 0
    return max(altura(raiz.esquerda), altura(raiz.direita)) + 1


def balanceada(raiz):
    if raiz is None:
        return True

    altura_esq = altura(raiz.esquerda)
    altura_dir = altura(raiz.direita)

    if abs(altura_esq - altura_dir) > 1:
        return False

    return balanceada(raiz.esquerda) and balanceada(raiz.direita)


def checa_simetrica(raiz):
    def simetricas(subarvore_esq, subarvore_dir):
        if not subarvore_esq and not subarvore_dir:
            return True
        elif subarvore_esq and subarvore_dir:
            return (subarvore_esq.chave == subarvore_dir.chave and
                    simetricas(subarvore_esq.esquerda, subarvore_dir.direita) and
                    simetricas(subarvore_esq.direita, subarvore_dir.esquerda))
        return False

    return not raiz or simetricas(raiz.esquerda, raiz.direita)
