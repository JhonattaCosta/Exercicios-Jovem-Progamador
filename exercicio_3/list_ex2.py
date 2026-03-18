num1 = (int(input("Digite um numero: ")))
num2 = (int(input("Digite um numero: ")))
num3 = (int(input("Digite um numero: ")))
num4 = (int(input("Digite um numero: ")))

listaNumeros = []

listaNumeros.append(num1)
listaNumeros.append(num2)
listaNumeros.append(num3)
listaNumeros.append(num4)
print(listaNumeros)

alvo = int(input("Digite um numero para remover se tiver na lista: "))

alvo in listaNumeros and listaNumeros.remove(alvo);
print(listaNumeros)