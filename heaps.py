def menor_elemento(a):
    return a[1]


def filho_esquerda(a, i):
    return a[2 * i]


def filho_direita(a, i):
    return a[2 * i + 1]


def pai(a, i):
    return a[i // 2]


def eh_heap(a):
    for i in range(2, len(a)):
        if a[i] > a[i // 2]:
            return False
    return True


def promove(a, n):
    i = n
    while True:
        if i == 1:
            break
        p = i // 2
        if a[p] >= a[i]:
            break
        a[p], a[i] = a[i], a[p]
        i = p


def demove(a, n):
    i = 1
    while True:
        c = 2 * i

        if c > n:
            break

        if c + 1 <= n:
            if a[c + 1] > a[c]:
                c += 1

        if a[i] <= a[c]:
            break

        a[c], a[i] = a[i], a[c]
        i = c
