#resumindo: os conjuntos são criados a partir de:
a = set()
#se adiciona usando:
b = 10
a.add(b)
a.add(11)
print(a)
#são representados por: {10}
#se unem com |
c = set()
c.add(11)
c.add(9)
print(c)
d = a | c #vai juntar eles
print(d)

#para mostrar os valores que estão em 1 que não aparecem no outro usa: 
print(a-c)

#para mostrar os números que são iguais nos dois conjuntos:
print(a - (a - c)) # vai mostrar os elementos em a tirando os que são diferentes, ou seja, os iguais

#posso transformar as listas em conjuntos também
a = [0, 1, 2, 3, 4, 5]

print(set(a))

#OS CONJUNTOS NÃO REPETEM VALORES E COLOCAM OS VALORES EM ORDEM CRESCENTE