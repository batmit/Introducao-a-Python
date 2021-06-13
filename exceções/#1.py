# agora veremos exeções
# são situações não previstas no código
# IndexError é um tipo de exeção, quando o valor da lista é menor que o procurado
# o ValueError é um erro que acontece quando trocamos int for str e assim por diante
# veja o exemplo:
nomes = ['Ana', 'Carlos', 'Maria']
for tentativa in range(3):
    try: # tente:
        i = int(input('Digite o índicie que quer imprimir: '))
        print(nomes[i -1])
    except ValueError: # a não ser que ocorra um ValueError
        print("Digite um Número! ")
    except IndexError: # a não ser que ocorra um IndexError
        print("Valor inválido, digite entre - 3 e 3")

        # veja o #2.py para ver o bloco Exception