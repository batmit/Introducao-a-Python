tabela = {
    'Alface': 0.45,
    'Batata': 1.20,
    'Tomate': 2.30,
    'Feijão': 1.50 
    #lembrar que os valores booleans, ponto flutuante, no python, usam ponto e não vírgula.
}
chaves = []
valores = []
for c in tabela:
    print(c) # mostra as chaves
    chaves.append(c)
    print(tabela[c]) # mostra os valores
    valores.append(tabela[c])
print(chaves, valores)

# gênio demais meu bom

#lembrando que eu poderia simplesmente:
#chaves = list(tabela.keys())
#valores = list(tabela.values())