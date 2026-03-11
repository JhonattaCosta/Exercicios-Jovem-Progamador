num = int(input("Digite a quantidade de horas: "))
if num < 24:
    print("A quantidade de horas tem que ser maior de 24")
    num = int(input("Digite a quantidade de horas: "))
num/=24
print("A quantidade de dias é: ", num, " Dias")