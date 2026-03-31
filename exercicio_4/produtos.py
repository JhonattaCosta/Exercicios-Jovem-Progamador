catalogo = []
estoque = {}

for i in range(3):
    id = i
    nome = input("Digite o nome do produto: ")
    valor = float(input("Digite o valor do produtor: (ex: 17.50)"))
    catalogo.append((id,nome,valor))
    pass

print(catalogo)
print(type(catalogo))
print(type(catalogo[0]))


for i in range(len(catalogo)):
    print(catalogo[i])
    qnt = int(input("Digite a quantidade do produto: "))
    idProduto = catalogo[i][0]
    estoque[idProduto] = qnt
    pass

print(estoque)
print(type(catalogo))

for i in range(len(catalogo)):
    buscaId = int(input("Digite um id para atular o valor e dar desconto: "))
    if buscaId == catalogo[i][0]:
        valorDesconto = int(input("Digite um valor para desconto: (ex: 10 para 10%)"))
        id, nome, valorAntigo = catalogo[i]
        valorNovo = valorAntigo * (1 - (valorDesconto / 100))
        catalogo[i] = (id, nome, valorNovo)
        print(f"Valor antigo era de:  {valorAntigo}  Agora ficou:  {valorNovo:.2f}")
    else:
        print("ID não existe tente novamente!")

carrinho = []
buscaId = input("Digite um id: ")

# for i in estoque:
#     if buscaId == estoque[i]:
#         elif estoque[id]>= qnt:
#             print("adicionar a tupla no carrinho (id, qnt, valorUnitário)")
#             print("descontar quantidade do estoque")
# 	    elif estoque[id]< qnt:
# 		    print("não tem em estoque")
#     else:
#         print("ID não foi encontrado!")
# 	print(carrinho)
# 	print(estoque)



