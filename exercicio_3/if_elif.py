peso = float(input("Digite seu peso: (ex: 78.6) "))
altura = float(input("Digite sua altura: (ex: 1.75) "))
imc = peso / (altura * altura)

if imc < 18.5:
    print("seu IMC é de: ",imc," seu grau é de Magreza")
elif imc < 25:
    print("seu IMC é de: ",imc," seu grau é de Normal")
elif imc < 30:
    print("seu IMC é de: ",imc," seu grau é de Sobrepeso")
else:
    print("seu IMC é de: ",imc," seu grau é de Obesidade")