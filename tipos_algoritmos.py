def fatorial(n):
    if n == 0:
        return 1
    return n * fatorial(n - 1)


def fib(n):
    if n <= 1:
        return n
    return fib(n - 1) + fib(n - 2)


def fib2(n):
    if n <= 1:
        return n
    fib_n_menos_2 = 0
    fib_n_menos_1 = 1
    for i in range(2, n):
        fib_n = fib_n_menos_1 + fib_n_menos_2
        fib_n_menos_2 = fib_n_menos_1
        fib_n_menos_1 = fib_n
    return fib_n_menos_1 + fib_n_menos_2


def hanoi(n, origem, destino, aux):
  # Caso base: movendo um disco.
    if n == 1:
        print("Mova de {} para {}".format(origem, destino))
    else:
        # Movendo n - 1 discos de 'origem' para 'aux'.
        hanoi(n - 1, origem, aux, destino)
        # Movendo um único disco de 'origem' para 'destino'.
        hanoi(1, origem, destino, aux)
        # Movendo os n - 1 discos de 'aux' para 'destino'.
        hanoi(n - 1, aux, destino, origem)


def fatorial_iterativo(n):
      fatorial = 1
      for i in range(1, n + 1):
        fatorial = fatorial * i
      return fatorial
