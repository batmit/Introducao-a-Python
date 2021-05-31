# os conjuntos (set) são uma ordem de agrupamento que realizam operações de união, intersecção e diferença
#ela não adimite a repetição de elementos e são mantidos em ordem numérica
a = set()
a.add(1)
a.add(2)
a.add(4)
a.add(3)
a.add(1) # como o 1 já está não vai mudar nada
a.add(-1) # os negativos ficam depois dos inteiros
a.add(-10)
a.add(0)
b = 100, 200 , 300
a.add(b)
print(a)

lista = [102, b]
print(lista)
a = set(lista) # vai colocar em ordem alfabética
print(a)