tabela = {

    'Alface': 0.45,
    'Batata': 1.20,
    'Tomate': 2.30,
    'Feijão': 1.50 
    
    #lembrar que os valores booleans, ponto flutuante, no python, usam ponto e não vírgula.
}
while True:
    nome = input("Digite uma chave para ser adicionada(0 sai): ")
    if nome == "0":
        break
    valor = float(input("Digite um valor para a chave: "))
    tabela[nome] = valor # jeito diferente de adicionar, mostra o quanto python é esperto
    # a partir de agora o nome vai receber o valor, o nome se tornou a chave, o nome não recebe mais potato, recebe 2.50
    print(tabela)