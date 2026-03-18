nome = input("Digite o nome do produto: ")
preco = float(input("Digite o preço do produto: "))
quantidade = int(input("Digite a quantidade: "))

produto = {}

produto["nome"] = nome
produto["preco"] = preco
produto["quantidade"] = quantidade

print(produto)

#Aumento de 5%
produto["preco"] = 1.05 * preco

print(produto)

print("Calculo total de Preço * quantidade é: ", produto["preco"]*produto["quantidade"])