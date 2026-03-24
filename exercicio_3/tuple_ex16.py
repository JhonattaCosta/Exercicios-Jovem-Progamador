nota1 = float(input("Digite uma nota: "))
nota2 = float(input("Digite outra nota: "))
nota3 = float(input("Digite outra nota: "))

notas = (nota1,nota2,nota3)

print(notas)
media = sum(notas) / len(notas)
print("Media da notas é: ", media)

