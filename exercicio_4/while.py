valores = []
num = 1
while num != 0:
    num = int(input("Digite o valor da compra: "))
    valores.append(num)
    print(valores)

print("O valor total é de: R$",float(sum(valores)))
print("A quantidade total é de: ",len(valores))
print(f"O valor medio gasto foi de: R${ float(sum(valores) / len(valores)):.2f}")