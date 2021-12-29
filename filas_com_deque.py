from collections import deque

fila = deque(["Banana", "Maçã", "Pera"])
print("Fila: ", fila)

fila.append("Uva")
print("Adicionando um elemento: ", fila)

fila.popleft()
print("Removendo um elemento: ", fila)
