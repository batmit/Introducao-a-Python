def imprime_lista(L, impressão, condição):
    for e in L:
        if condição(e):
            impressão(e)
def imprime_elemento(e):
    print(f"Valor: {e}")
def épar(x):
    return x % 2 == 0
def éimpar(x):
    return not épar(x) # vai verificar o resultado e retornar the opposite, if it´s no par it´s impar
L = [1, 7, 9, 2, 11, 0]
imprime_lista(L, imprime_elemento, épar)
imprime_lista(L, imprime_elemento, éimpar)