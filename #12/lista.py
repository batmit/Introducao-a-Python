# operações de empacotamento também funcionam com listas, como:
a, b = [1, 2]
print(a)
print(b)
print("-=-" * 10)
#para especificar que queremos desempacotar muitos valores usamos:
*a, b = [1, 2, 3, 4, 5, 6]
print(a)
print(b)
print("-=-" * 10)
a, *b = [1, 2, 3, 4, 5, 6]
print(a)
print(b)
print("-=-" * 10)
# com esse asterisco eu pego todos os valores e deixo 1 para o outro, o primeiro se o outro vier antes da virgula e o último de vier depois
#ele vai sempre deixar um com cada variável e o resto com a variável do asterisco
a, *b, c = [1, 2, 3, 4, 5, 6, 7]
print(a)
print(b)
print(c)

#esse é um meio de divisão de espaço muito bom e inteligente