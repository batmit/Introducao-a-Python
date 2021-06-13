# as funções lambda são versões bem simples de funções
a = lambda a, b: print(a + b) # a é a variável que recebe a função, lambda é para definir, a, b sãp parâmetros
# tudo depois do : é a execução da função
a(10, 20)


aumento = lambda a = 10, b = 20: (a * b / 100) # 0 a e b já vem com valores pré progamados
print(aumento())
print(aumento(100, 5))

