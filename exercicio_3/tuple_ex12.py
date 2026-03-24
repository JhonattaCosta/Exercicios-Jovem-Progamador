fruta1 = input("Digite uma fruta: ")
fruta2 = input("Digite uma fruta: ")
fruta3 = input("Digite uma fruta: ")

frutas = (fruta1, fruta2, fruta3)

fruta = input("Digite um nome de fruta para verificar se esta presente: ")

print("Esta presente? ", fruta in frutas)