#podemos colocar listas dentro de dicionários
estoque = {
    "tomate": [1000, 2.30],
    'alface': [500, 0.45],
    "batata": [2001, 1.20],
    "feijão": [100, 1.50]
}
venda = [["tomate", 5], ['batata', 10], ["alface", 5]]
total = 0
print("Vendas: \n")
for operação in venda:
    produto, quantidade = operação #produto recebe a chave e quantidade o 5 ou 10
    preço = estoque[produto][1]
    custo = preço * quantidade
    print(f"{produto:12s}: {quantidade:3d} x {preço:6.2f} = {custo:6.2f}")
    estoque[produto][0] -= quantidade
    total += custo
print(f"Custo total: {total:21.2f}")
print(f"Estoque: \n")
for chave, dados in estoque.items(): # seleciono tanto as chaves quanto os valores
    print("Descrição: ", chave)
    print("Quantidade: ", dados[0])
    print(f"Preço: {dados[1]:6.2f}\n")
