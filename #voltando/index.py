# o find não pode ser usado em listas, logo usamos index e rindex
l = [ 0, 1, 2,3 ,4 ,4, 5, 5, 5]
a = l.index(4)
print(a)
print(l.index(4, a + 1)) # vou procurar o 4 a partir da posição a + 1, o primeiro quatro