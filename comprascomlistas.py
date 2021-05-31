compras = []
while True:
    produto = input("Produto(fim termina): ")
    if produto == 'fim':
        break
    quantidade = int(input("Quantidade: "))
    preço = float(input("Preço: "))
    compras.append([produto, quantidade, preço]) # adicionou 1 item a lista, uma lista sobre lista 
    # na parte de cima eu vou adicionar produto, quantidade e preço tudo em forma de uma lista só dentro da lista compras
    # se eu por exemplo colocar 3 produtos, o len de compras não vai ser 9 e sim 3(tem 3 listas com 3 itens em cada lista)
soma = 0
print("_-_" * 100)
for e in compras: # esse e é a quantidade de listas que tem em cada um. Esse e contém dentro de sí o produto, a quantidade e o preço
    p = e[1] * e[2] # pega o e na posição que fala na posição do compras
    print(f"\n Produto: {e[0]}\n Quantidade: {e[1]}\n Preço de cada um: {e[2]:.2f}")
    soma += e[1] * e[2]
print(f"\nPreço final: {soma:7.2f}")
#print(compras) # se você fizer um len de compras vai ver a quatidade de listas que tem nele.
# o e na primeira repetição vai ser ["batata", 2, 40.0] esse é o compras[0], e a primeira repetição do e