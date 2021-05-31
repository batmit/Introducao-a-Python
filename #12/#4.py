#embora não podemos alterar uma tupla após sua criação, podemos concatená-las:
t1 = (1, 2, 3)
t2 = (4, 5, 6)
t3 = t1 + t2
print(t3)

#agoraaaa, se tiver uma lista nessa tupla podemos alterar a lista:

tupla = ("a", ["b", "c", "d"])
print(tupla)
print(len(tupla))

print(tupla[1])
tupla[1].append("e")
print(tupla)
# a lista não foi alterada, apenas a lista que ela tinha, isso é interessante, posso usar isso e depois converter tudo numa lista