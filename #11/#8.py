# para deletar usamos a função del mesmo
tabela = {
    'Alface': 0.45,
    'Batata': 1.20,
    'Tomate': 2.30,
    'Feijão': 1.50 
    #lembrar que os valores booleans, ponto flutuante, no python, usam ponto e não vírgula.
}

print(tabela.keys())

le = input("Digite a chave para apagar: ")

a = tabela.pop(le) # posso usar o del também. O pop salva o tabela[le], ou seja, o valor da chave e não a chave me si
print(a)
print(le)
print(tabela)     

# as listas são mais maleáveis e fáceis de mexer
