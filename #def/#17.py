# vimos os parâmetros opicionais, que já são pré-definidos mas que podem mudar
# agora vamos ver que podemos chmar os parâmetros num ordem aleatória especificando eles
def retângulo(largura=37, altura=10, caractere="*"): # recebo largura e altura como opicionais e caractere como obrigatório
    linha = caractere * largura # o linha vai ser o número da largura vezes o caractere
    for i in range(altura): # coloco um range que recebe o valor de altura
        print(linha) # imprimo a linha
retângulo()
retângulo(37, 10)
retângulo(altura=10, largura=37, caractere="-") # aqui eu inverti a ordem, lembrando que se eu mudar a ordem de
# um eu devo mudar a ordem de todos.
retângulo(caractere="|", largura=37, altura=10)
