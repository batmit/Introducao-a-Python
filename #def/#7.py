def soma(L):# função soma recebe a lista L
    total = 0 # total = 0
    for e in L:# vai repetir todos os valores dentro de L
        total += e # vai soma-los
    return total # vai retornar o valor da soma

def média(X): # a função media recebe uma lista
    return soma(X) / len(X) # vou retonar a função soma recebendo o L dividido pelo len(L)
    # mesmo eu colocando soma(X) ainda deu, isso porque eu envio X para a função soma
batata = [10, 20, 30, 40, 0, 50]
print(média(batata)) # o L recebe batata
# lembrar que sempre que executamos o return a função para, é interrompida