orcamento = float(input("Digite o valor do orçamento: "))
gasto = float(input("Digite o valor do gasto: "))

if orcamento < 0:
    print("Valor do orçamento não pode ser negativo, digite o valor novamente: ")
    orcamento = float(input("Digite o valor do orçamento: "))
if gasto < 0:
    print("Valor do gasto não pode ser negativo, digite o valor novamente: ")

print("Valor do orçamento era de : R$", orcamento, "valor do gasto foi de: R$", gasto)
orcamento-=gasto
print("Valor do orçamento atual é de: ", orcamento)