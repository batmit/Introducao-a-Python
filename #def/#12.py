#validação
# elas são importante para evitar erros mais tarde nos valores usados
def validação(pergunta, mínimo, máximo):
    while True:
        v = int(input(pergunta))
        if v > máximo or v < mínimo:
            print("Valor inválido, tente novamente")
        else:
            return v # se for verdadeiro retorno o v e acaba a repetição
            #lembrando que o return ele acaba com a função, dá unm break
print(validação("Número menor que 10 e maior que 1: ", 1, 10))
# sempre verificar os valores recebidos para não dar nenhum erro futuro