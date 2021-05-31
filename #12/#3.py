# para ser uma tupla com apenas um valor DEVEMOS adicionar uma vírgula, como:

t1 = (1) # isso não é uma tupla, é uma variável
print(t1)

t2 = (1,) # isso é uma tupla
print(t2)

t3 = 1, # isso também é uma tupla, não precisamos usar parênteses
print(t3)

#tem como criar uma tupla vazia:

t4 = ()
print(len(t4))

#assim como podemos transformar uma lista em tupla:

l = [1, 2, 3]
t = tuple(l)
print(t)
