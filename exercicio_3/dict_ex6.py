nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))

aluno = {}

aluno["nome"] = nome
aluno["idade"] = idade

print(aluno)
print(type(aluno))
print(type(aluno["nome"]))
print(type(aluno["idade"]))

