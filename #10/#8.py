compras = []
while True:
    produto = input("Produto comprado(0 para terminar): ")
    if produto == '0':
        print("Fim")
        break
    compras.append(produto)
print("Produtos comprados: ")
for p in compras:
    print(p)