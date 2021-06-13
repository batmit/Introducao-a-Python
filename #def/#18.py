def soma(x ,y):
    return x + y
def subtração(x, y):
    return x - y
def função(a, b, func=soma): # soma é o parâmetro padrão, pode ser modificado
    print(func(a, b)) # vou passar a função a ser utilizada como parâmetro
função(5, 4, soma)
função(10, 5, subtração)