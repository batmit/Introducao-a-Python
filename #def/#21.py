# podemos usar funções bem simples chamadas de lambda
a = lambda x: x * 2 # x: recebe o x e usar ele
print(a(3))

# a = lambda x : x * 2
# o a é o nome, a variável que recebe a função, colocamos lambda para demonstrar que é uma função desse tipo,
# passamos o x como parâmetro e dentro realizamos a operação x * 2

aumento = lambda a= 2, b= 1: print((a * b / 100)) # recebe o a e b como parâmetros e realiza a operação
aumento(a= 100, b= 5)
aumento()

# nome da função = lambda + parâmetros: execução