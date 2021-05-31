a = [1, 2, 3, 4, 5, 6]
b = [4, 5, 6, 7]
b = set(b) # vou ter que transformar em conjuntos primeiros
a = set(a)
comuns = a - (a - b) 
print("Lista1: ", a, "\nLista2:", b)
print("Os valores comuns: ", comuns)
print("Os valores que a primeira tem que a segunda não tem: ", a-b)
print("Os valores que existem apenas na segunda: ", b-a)