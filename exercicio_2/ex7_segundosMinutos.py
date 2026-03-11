segundos = int(input("Digite a quantidade de minutos "))

if segundos < 60:
    print("Quantidade de minutos é menor que 60 ou seja uma hora tente novamente.")
    segundos = int(input("Digite a quantidade de minutos "))
minutos = segundos // 60
print("Quantidade de é: ", minutos, "Minutos")