#podemos colocar listas dentro de dicionários
estoque = {
    "tomate": [1000, 2.30],
    'alface': [500, 0.45],
    "batata": [2001, 1.20],
    "feijão": [100, 1.50]
}
print()
print(f"Produtos em estoque: {estoque.keys()}")
print()
venda = []
while True:
    comprado = input("Qual desses produtos você deseja comprar?(0 para sair da repetição) ")
    if comprado == '0':
        break
    quantidadecompra = int(input("Qual a quantidade? "))
    venda.append([comprado, quantidadecompra]) # eu adiciono em forma de lista o produto e a quantidade
total = 0
print()
print("Vendas: ")
for operação in venda:
    produto, quantidade = operação #produto recebe o valor[0] da venda, e quantidade recebe [1]
    preço = estoque[produto][1]
    custo = preço * quantidade
    print(f"{produto:12s}: {quantidade:3d} x {preço:6.2f} = {custo:6.2f}")
    estoque[produto][0] -= quantidade
    total += custo
print(f"Custo total: {total:21.2f}")
print()
print(f"Estoque: ")
for chave, dados in estoque.items(): # seleciono tanto as chaves quanto os valores
    print("Descrição: ", chave)
    print("Quantidade: ", dados[0])
    print(f"Preço: {dados[1]:6.2f}\n")