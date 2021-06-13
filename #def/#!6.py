#veja uma fução que não precisa de valores para ser executada:
def barra():
    print("*" * 40)
# também podemos fazer com valors pré-estabelecidos na função, mas que podem ser alterados:
def barra2(n=40, caracteres="*"): # os valores já estão mas podem mudar se eu chamar um diferente
    print(caracteres * n )
barra2()# vai chamar com os valores estabeçecidos
barra2(100) # vai alterar o primeiro valor
barra2(100, "-") # vai alterar ambos os valores

#também podemos misturar parâmetros opicionais com obrigatórios
def soma(a, b, imprime=False): # a e b são obrigatórios para funcionarm imprime não é obrigatório
    # não posso colocar o parâmetro opicional antes dos obrigatórios, senão teria de preencher o opicional
    s = a + b
    if imprime:
        print(s)
    return s
soma(10, 20)
soma(10, 20, True)