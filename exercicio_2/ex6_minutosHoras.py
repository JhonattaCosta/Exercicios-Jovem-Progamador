minutos = int(input("Digite a quantidade de minutos "))

if minutos < 60:
    print("Quantidade de minutos é menor que 60 ou seja uma hora tente novamente.")
    minutos = int(input("Digite a quantidade de minutos "))
horas = minutos // 60
print("Quantidade de hora é: ", horas," Horas")