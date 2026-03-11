valorEstoque = int(input("Digite a quantidade de estoque"))
valorVenda = int(input("Digite a quantidade de vendas:"))
reposicao = int(input("Digite a quantidade de reposição do estoque: "))

print("Valor inicial do estoque: ", valorEstoque)
valorEstoque -= valorVenda
print("Valor do estoque depois da venda de ", valorVenda, " ficou com ", valorEstoque)
valorEstoque += reposicao
print("Reponto com ", reposicao, "Estoque ficou com valor de ", valorEstoque)
valorEstoque %= 6
print("valor final do estoque é: ",valorEstoque)