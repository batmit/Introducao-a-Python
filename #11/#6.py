tabela = {
    'Alface': 0.45,
    'Batata': 1.20,
    'Tomate': 2.30,
    'Feijão': 1.50 
    #lembrar que os valores booleans, ponto flutuante, no python, usam ponto e não vírgula.
}

chave = input("Digite uma chave para ser adicionado ao dicionário: ")
valor = input("Digite um valor para ser adicionado a chave anterior: ")

tabela[chave] = valor # a chave vai receber o valor na última posição

print(tabela)
print("_+_" * 100)
chave2 = input("Digite uma chave para ser adicionado ao dicionário: ")
valor2 = input("Digite um valor para ser adicionado a chave anterior: ")

tabela2 = {

    chave2: valor2

}

print(tabela2) # deu direitinho

