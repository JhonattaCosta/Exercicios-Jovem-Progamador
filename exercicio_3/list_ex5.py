fila = ["Ana", "Bruno"]

nome1 = input("Digite um nome: ")
nome2 = input("Digite outro nome: ")

fila2 = []

fila2.append(nome1)
fila2.append(nome2)

print(fila2)

fila.extend(fila2)

print(fila)

prioritario = input("digite o nome do cliente prioritário: ")

fila.insert(1, prioritario)

print(fila)

atendido = fila.pop(0)

print("Fila atual: ", fila, "Atendido por ultimo: ", atendido)