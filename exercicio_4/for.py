numbers = []

for i in range(10):
    num = int(input("Digite um numero: "))
    numbers.append(num)

for i in numbers:
    if numbers[i] > 10:
        print("Numero ", numbers[i], " é maior que 10")
    elif numbers[i] == 10:
        print("Numero ", numbers[i], " é igual a 10")
    else:
        print("Numero ", numbers[i], " é menor que 10")