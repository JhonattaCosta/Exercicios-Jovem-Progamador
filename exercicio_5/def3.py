def par_impar(num):
    if num % 2 == 0:
        print("Numero ", num, " é par")
    else:
        print("Numero ", num, " é impar")

num = int(input("Digite um numero inteiro para saber se é par ou impar: "))

par_impar(num)