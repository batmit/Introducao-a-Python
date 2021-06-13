# o bloco de tentativas abaixo é o
nomes = ["Ana,", 'Paula', 'Maria']
for tentativa in range(len(nomes)):
    try:
        i = int(input('Digite o índicie que quer imprimir: '))
        print(nomes[i -1])
    except Exception as e: # o Excepition inclue todos os erros possíveis
        print(f"Algo de errado aconteceu: {e}")