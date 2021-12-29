import random
# Exemplo: Contar elementos duplicados
# Complexidade O(n²)
def encontra_elementos_duplicados(lista, m):
    if not lista:
        return []

    duplicatas = []
    for i in range(len(lista)):
        for j in range(i + 1, len(lista)):
            if lista[i] == lista[j]:
                duplicatas.append(lista[j])

    return duplicatas

# Complexidade O(n)
def encontra_elementos_duplicados_frequencia(lista, m):
    if not lista:
        return []

    tabela_frequencia = [0] * m
    duplicatas = []
    for elemento in lista:
        tabela_frequencia[elemento] += 1
        if tabela_frequencia[elemento] > 1:
            duplicatas.append(elemento)

    return duplicatas


# Exemplo: Inverter um arranjo

def inverte(nums):
    inicio = 0
    fim = len(nums) - 1
    while inicio < fim:
        nums[inicio], nums[fim] = nums[fim], nums[inicio]
        inicio += 1
        fim -= 1
    return nums


def confere_inversao(n, m):
    for _ in range(n):
        nums1 = [random.randint(0, m) for _ in range(m)]
        nums2 = list(nums1)
        nums1.reverse()

        assert(inverte(nums2) == nums1)

    print("Sucesso!")


# Exemplo: Mover zeros
def move_zeros_tres_etapas(nums):
    zeros = nums.count(0)
    if zeros == 0:
        return nums

    atual = 0
    for i, num in enumerate(nums):
        if num != 0:
            nums[atual] = nums[i]
            atual += 1

    tamanho = len(nums) - 1
    for i in range(zeros):
        nums[tamanho - i] = 0

    return nums


def move_zeros(nums):
    sentinela = 0
    for i, num in enumerate(nums):
        if num != 0:
            nums[sentinela], nums[i] = nums [i], nums[sentinela]
            sentinela += 1
        print("Iteração " + str(i) + ": Lista de entrada: " + str(nums))
    return nums


print("Lista final: ", move_zeros([0, 1, 0, 3, 12]))
