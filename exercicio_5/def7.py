def palindromo(palavra):
    palavra_limpa = palavra.lower().replace(" ","")
    if palavra_limpa == palavra_limpa[::-1]:
        print(f" '{palavra}' É um palindromo!")
    else:
        print(f" '{palavra}' Não é um palindromo!")

palindromo("arara")
palindromo("Python")
palindromo("Ana")
