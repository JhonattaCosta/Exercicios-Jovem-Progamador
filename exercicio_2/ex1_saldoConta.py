saldoConta = float(input("Digite o saldo da sua conta: "))
valorDeposito = float(input("Digite o valor do deposito: "))

if saldoConta < 0:
    print("Valor do saldo tem que ser maior que 0! ")
    saldoConta = float(input("Digite o saldo da sua conta: "))
if valorDeposito < 0:
    print("Valor do reposito tem que ser maior que 0! ")
    valorDeposito = float(input("Digite o valor do deposito: "))


print("Valor depositado foi de: R$", valorDeposito, " seu saldo era de: R", saldoConta)
saldoConta+=valorDeposito
print("Seu novo saldo é de: R$", saldoConta)