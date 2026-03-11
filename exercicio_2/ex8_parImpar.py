num = int(input("Digite um numero para saber se é impar ou par: "))
num %= 2
if num == 0:
    print("numero é Par")
elif num == 1:
    print("Numero é Impar")