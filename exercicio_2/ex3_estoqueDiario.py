qntEstoque = int(input("Qual a quantidade em estoque ?"))
if qntEstoque < 0:
    print("Estoque não pode ser negativo")
    qntEstoque = int(input("Qual a quantidade em estoque ?"))


qntVendida = int(input("Quantos produtos foram vendidos?"))


if qntVendida < 0:
    print("Quantidade vendida não pode ser negativa")
    qntVendida = int(input("Quantos produtos foram vendidos?"))

print("Tinhamos em estoque ", qntEstoque, " e Foram vendidos ", qntVendida)
qntEstoque-=qntVendida
print("Agora temos o total de ", qntEstoque, " de produtos no estoque")