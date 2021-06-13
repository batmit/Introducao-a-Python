# o bloco de tentativas abaixo é o
nomes = ["Ana,", 'Paula', 'Maria']
for tentativa in range(len(nomes)):
    try:
        i = int(input('Digite o índicie que quer imprimir: '))
        print(nomes[i -1])
    except Exception as e: # o Excepition inclue todos os erros possíveis
        # o interessante é que eu coloco o Excepition as e, ou seja, eu pego
        # o erro que deu e coloco em uma variável que posso acessar depois
        print(f"Algo de errado aconteceu: {e}")

# para revisar: Excepition as e contém todos os valores de erro, ele então coloca
# na variável e o erro que deu, Excepition as e