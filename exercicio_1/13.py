salario = float(input("Digite o salario: "))
percentual = float(input("Digite o percentual de aulmento: "))
aumento = salario + (salario * percentual / 100)
print("O salario era de: R$", salario, " com aumento foi para: R$", aumento)