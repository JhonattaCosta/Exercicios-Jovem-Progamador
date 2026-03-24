num1 = int(input("Digite um numero: "))
num2 = int(input("Digite outro numero: "))
num3 = int(input("Digite outro numero: "))
num4 = int(input("Digite outro numero: "))

numeros = (num1, num2, num3, num4)

num = int(input("Digite um numero para ver quantas vezes eles se repete"))

print("O numero: ", num , " se repete ", numeros.count(num), " veses!" )

