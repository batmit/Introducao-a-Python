def pesquise(lista, valor):
    if valor in lista:
        return lista.index(valor) # IMPORTANTE => o find não pode ser usado em listas, apenas o index
    return None

L=[10, 20, 25, 30]
print(pesquise(L, 25))
print(pesquise(L, 27))