#for c in range(5, 8):
#    print(c)
while True:
    l = int(input("Digite um número de valores para imprimir(0 dá o break): "))
    if l == 0:
        break
    for c in range(0, l + 1):
        print(c)