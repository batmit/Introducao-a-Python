a = [0, 1, 2, 3, 4, 5, 6]
b = [2, 3, 4, 5, 6, 7, 8]

a = set(a)
b = set(b)
print("Lista1: ", a, '\nLista2: ', b)
print("Os elementos que não mudaram: ", b-(b-a)) # iguais
print("Novos elementos: ", b-a) # diferentes
print("Elementos que foram removidos: ", a-b) # removidos