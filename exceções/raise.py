# o raise é outro tipo de exceção
nomes = ["Ana", 'Carlos', 'Maria']
try:
    i = int(input('Digite o índicie que quer imprimir: '))
    print(nomes[i - 1])
except ValueError as e:
    print('Digite um número!')
    raise # o raise mostra o código de erro
finally:# o finally é executado sempre
    print("O finally é sempre executado")