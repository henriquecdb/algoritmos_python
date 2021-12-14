def algoritmo_a(n):
    s = 0
    for i in range(1, n + 1):
        for j in range(i, n + 1):
            s = s + 1
    return s


def algoritmo_b(n):
    s = 0
    for i in range(1, n + 1):
        s = s + i
    return s


def algoritmo_c(n):
    return n * (n - 1) // 2
