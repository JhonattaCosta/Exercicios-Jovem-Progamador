agenda = {"nome":"Jhonatta","telefone":"1111-1111"}
agenda2 = {"nome":"Lidiane","telefone":"2222-2222"}

print(agenda)
print(agenda2)

nome = input("Digite o nome da pessoa que quer atualizar")
telefone = input("Digite o telefone da pessoa que quer atualizar")

if nome == agenda["nome"]:
    agenda["telefone"] = telefone
elif nome == agenda2["nome"]:
    agenda2["telefone"] = telefone
else:
    print("Usuario não existe")

print(agenda)
print(agenda2)