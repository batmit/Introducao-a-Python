def pesquise(lista, valor):
    for x, e in enumerate(lista):
        if e == valor:
            return x + 1, e # assim que retornar vai acabar a repetição
    else: # se nada acontecer
        return None
L = [ 10, 20, 25, 30]
print(pesquise(L, 25))
print(pesquise(L, 27))# vai retornar None