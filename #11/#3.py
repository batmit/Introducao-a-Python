# os dicionários é composto por um conjunto de chaves e valores
# os dicionários consistem em relacionar uma chave com um valor

tabela = {
    'Alface': 0.45, # não chega a ser um recebe
    'Batata': 1.20,
    'Tomate': 2.30,
    'Feijão': 1.50 
    #lembrar que os valores booleans, ponto flutuante, no python, usam ponto e não vírgula.
}
# 'Alface' é uma chave e 0.45 é um valor
print(tabela['Alface']) #devemos colocar em '' pois é a chave, 'alface' é uma chave que recebe o valor 0.45

#nas chaves, diferentemente das listas, não usamos o índicie como número, mas sim a chave
print(tabela)

tabela['Cebola'] = 2.50 # eu crio uma nova chave isso na última posição

print(tabela)

tabela['Alface'] = 1.0

print(tabela['Alface'])

print("_+_" * 100)

print("Manga" in tabela) # se não tiver vai mostrar false
# variável lógica, variáveis desse tipo retornam apenas True ou False
print("Tomate" in tabela) # vai mostrar True e não o valor

# (     tabela["Alface"]         ) Eu seleciono a tabela e retorno o valor dentro da chave Alface
