catalogo = []

for i in range(3):
    id = int(input("Digite o id: (ex: 1 ou 2) "))
    nome = input("Digite o nome do produto: ")
    valor = float(input("Digite o valor do produtor: (ex: 17.50)"))
    catalogo.append((id,nome,valor))
    pass

print(catalogo)
print(type(catalogo))
print(type(catalogo[0]))

estoque = {}
num = 0
for i in range(3):

    print("Qual a quantidade inicial do produto: ", catalogo[num])
    qnt = int(input())
    estoque[catalogo[num]] = qnt
    num+=1

print(estoque, type(estoque))