tabela = {
    'Alface': 0.45,
    'Batata': 1.20,
    'Tomate': 2.30,
    'Feijão': 1.50 
    #lembrar que os valores booleans, ponto flutuante, no python, usam ponto e não vírgula.
}
# são métodos
print(tabela.keys()) # pegamos a tabela e adicionamos .keys que pega todas as chaves
print(tabela.values()) # pegamos a tabela e adicionamos .values que pega todos os valores

chaves = list(tabela.keys()) # transforma em uma lista, salva os valores na hora e não precisa usar for

print(a)