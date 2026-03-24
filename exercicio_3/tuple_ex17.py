num1 = int(input("Digite um numero: "))
num2 = int(input("Digite outro numero: "))
num3 = int(input("Digite outro numero: "))
num4 = int(input("Digite outro numero: "))

numeros = (num1,num2,num3, num4)
print("Tupla não ordenada: ", numeros)
print("Tupla ordenada: ", sorted(numeros))

print("Tipo: ", type(sorted(numeros)))