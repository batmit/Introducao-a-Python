estoque = {
    "tomate": [1000, 2.30],
    'alface': [500, 0.45],
    "batata": [2001, 1.20],
    "feijão": [100, 1.50]
}
venda = [["tomate", 5], ['batata', 10], ["alface", 5]] #aqui eu não pego os valores do tomate, só o nome

for c in venda:
    produto, quantidade = c # como tem duas variáveis na lista, pega o valor
    print(produto, '\n', quantidade)
 

for produto, quantidade in estoque.items():
    print(produto)
    print(quantidade)