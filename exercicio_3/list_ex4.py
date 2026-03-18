nota1 = float(input("Digite uma nota: "))
nota2 = float(input("Digite uma nota: "))
nota3 = float(input("Digite uma nota: "))

listaNotas = []

listaNotas.append(nota1)
listaNotas.append(nota2)
listaNotas.append(nota3)

print("A media é: ", (sum(listaNotas) / 3))



nota4 = float(input("Digite outra nota para subistituir a menor: "))

menorNota = float(min(listaNotas))
index = listaNotas.index(menorNota)

listaNotas[index] = nota4

listaNotas.sort()
print("Lista ordenada: ", listaNotas)

print("A media é: ", (sum(listaNotas) / 3))


